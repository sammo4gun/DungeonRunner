(define (domain door)
 (:requirements :adl :domain-axioms :intentionality :expression-variables :bardiche)
 (:types item character room)
 (:constants key axe - item
             gatehouse - room)
 
 (:predicates (has ?character - character ?item - item)
              (had ?character - character ?item - item)
              (at ?character - character ?room - room)
              (in ?item - item ?room - room)
              (adjacent ?room - room ?neighbor - room)
              (doorOpen)
  )
 
 (:action move
   :parameters      (?character - character ?from - room ?to - room)
   :precondition    (and (at ?character ?from) 
                         (adjacent ?from ?to)
                         (not (= ?from ?to)))
   :effect          (and (not (at ?character ?from))
                         (at ?character ?to))
   :agents          (?character)
   :initiator       (?character))
    
  (:action give
    :parameters     (?giver - character ?item - item ?receiver - character ?room - room)
    :precondition   (and (not (= ?giver ?receiver))
                         (not (had ?receiver ?item)) ;; no give backsies
                         (at ?giver ?room)
                         (at ?receiver ?room)
                         (has ?giver ?item))
    :effect         (and (not (has ?giver ?item))
                         (has ?receiver ?item))
    :agents         (?giver ?receiver)
    :initiator      (?giver))
    
  (:action take
    :parameters     (?taker - character ?item - item ?victim - character ?room - room)
    :precondition   (and (not (= ?taker ?victim))
                         (not (had ?taker ?item))
                         (at ?taker ?room)
                         (at ?victim ?room)
                         (has ?victim ?item))
    :effect         (and (not (has ?victim ?item))
                         (has ?taker ?item))
    :agents         (?taker)
    :initiator      (?taker))
    
  (:action pickup
    :parameters     (?character - character ?item - item ?room - room)
    :precondition   (and (at ?character ?room)
                         (in ?item ?room)
                         (not (had ?character ?item)))
    :effect         (and (not (in ?item ?room))
                         (has ?character ?item))
    :agents         (?character)
    :initiator      (?character))
    
  (:action open
    :parameters     (?character - character)
    :precondition   (and (at ?character gatehouse)
                         (or (has ?character key)
                             (has ?character axe)))
    :effect         (doorOpen)
    :agents         (?character)
    :initiator      (?character))
    
  (:axiom
    :vars           (?room - room ?neighbor - room)
    :context        (adjacent ?room ?neighbor)
    :implies        (adjacent ?neighbor ?room))
                         
  (:axiom
    :vars           (?character - character ?item - item)
    :context        (has ?character ?item)
    :implies        (had ?character ?item))
)