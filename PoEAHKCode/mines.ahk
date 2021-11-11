#IfWinActive, Path of Exile
#MaxThreadsPerHotkey 2


toggle	:= 0

return

F1::
	reload
	return

+F3::

	toggle	:= !toggle

	if (toggle = 0){
		; if toggle 0 (false) do shit in here
		ToolTip
		breaker := true
	}
	else{
		; if toggle 1 (true) do shit in here
		breaker := false
		Loop,
		{
			if (breaker = true){
				break
			}
    	ToolTip, Auto`nDetonating`nEnabled, 1530, 884
    	Random, t, 300, 600
    	Sleep, %t%
    	Send, {d down}
    	Random, s, 30, 60
    	Sleep, %s%
    	Send, {d up}
		}
	return
	}

return