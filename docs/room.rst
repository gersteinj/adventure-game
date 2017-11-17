Room
====
.. py:class:: Room(name, desc, north=True, east=True, south=True, west=True)

   Create a room. Assign False to a wall to remove the door
   
   .. py:attribute:: name
      
      Name of the room
   
   .. py:attribute:: walls
      
      Dictionary containing information about north, south, east, and west walls.

      {'north': True/False, 'south': True/False, 'east': True/False, 'west': True/False}

   .. py:attribute:: desc
      
      Description of the room
      
   .. py:method:: welcome()

      Welcome player to the room