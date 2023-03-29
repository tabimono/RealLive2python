label after_load:
  $ init_vars(False)
  return

label start:
  $ init_vars(True)
  # i = 1
  # effect = 101
  # title = "The title"

label start:
  
label __skip__1:
  "This is just the beginning"
  jump __skip__0
  
label __skip__0:
  "{fast}{nw}"
  $ renpy.scene()
  $ show_image(ns_state, "black", "bg")
  "... or is it ?"
  jump intro

label intro:
  $ renpy.scene()
  $ show_image(ns_state, "some/file/somewhere", "bg")
  "This is the intro"
  nvl clear
  jump __skip__1
