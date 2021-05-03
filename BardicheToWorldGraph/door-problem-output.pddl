(define (problem door)
  (:domain door)
  (:requirements :expression-variables)
  (:objects knight evil_knight prince - character
            bedroom armory hallway cell - room)
  (:init (had evil_knight apple)
         (adjacent hallway bedroom)
         (adjacent gatehouse hallway)
         (at prince gatehouse)
         (adjacent armory gatehouse)
         (doorOpen)
         (had knight axe)
         (adjacent gatehouse armory)
         (adjacent hallway cell)
         (intends evil_knight (has evil_knight key))
         (had evil_knight key)
         (intends evil_knight (not (doorOpen)))
         (has evil_knight key)
         (intends evil_knight (has evil_knight axe))
         (at evil_knight gatehouse)
         (adjacent hallway gatehouse)
         (intends evil_knight (has evil_knight apple))
         (has evil_knight apple)
         (at knight gatehouse)
         (adjacent cell hallway)
         (intends knight (doorOpen))
         (adjacent bedroom hallway)
         (has knight axe)
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