(define (problem door)
  (:domain door)
  (:requirements :expression-variables)
  (:objects knight evil_knight prince - character
            bedroom armory hallway cell - room)
  (:init (had evil_knight apple)
         (intends evil_knight (not (doorOpen)))
         (adjacent hallway bedroom)
         (adjacent gatehouse hallway)
         (adjacent armory gatehouse)
         (has evil_knight key)
         (intends evil_knight (has evil_knight axe))
         (adjacent gatehouse armory)
         (in axe armory)
         (adjacent hallway gatehouse)
         (adjacent hallway cell)
         (intends evil_knight (has evil_knight apple))
         (at knight cell)
         (at evil_knight cell)
         (has evil_knight apple)
         (intends evil_knight (has evil_knight key))
         (at prince bedroom)
         (adjacent cell hallway)
         (had evil_knight key)
         (intends knight (doorOpen))
         (adjacent bedroom hallway)
         (intends prince (has knight key))
         (had knight key)
         (intends prince (has knight apple)))
  (:goal (and (has knight axe)
              (doorOpen)))
  (:protagonist knight)

  (:bardichegoal
   (good 
    (and (has knight key) (doorOpen))
    (and (has knight axe) (doorOpen))
   )
   (bad 
    (and (has evil_knight axe) (has evil_knight apple) (has evil_knight key))
   )
  )
)