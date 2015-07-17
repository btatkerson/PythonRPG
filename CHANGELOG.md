<b>Updates</b>:

#######################################################################################
Jul 7, 2015

- This update is the beginning of having racial features added into the game. This will
  alter combat immediately and other things in-game down the line.

  "creature" is overall the most complete of the code stacks and is useable at a very
  basic levels, including simple combat! This is demonstrated in test_battle.py

+ Redid the race settings to actually have some structure, will soon implement into 
  the rest of the creature
+ Added size classes
+ Added the GPL v3 license

#######################################################################################
Jul 5, 2015
+ Added get_index to core constants
+ Changed from hard-coded creature experience tables and moved xp table into xptable.csv
+ XP earned is now generated from xptable.csv
+ Core constants added to creature race file

#######################################################################################
Jun 27, 2015
+ Added average roll parameter to dice class
+ Dice class now acts as a functor for default sides/occurances 
+ Creature race retabbed and unneccessary components were removed


