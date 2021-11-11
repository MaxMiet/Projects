Loop, 3
    InitOnlyOnce(A_Index)
Return
    
InitOnlyOnce(Index){
  static init=0, text
  
  If !(init++){      
      Clipboard:= 
  }
}

#Persistent
OnClipboardChange:
Sleep, 100
Xex()
return

Xex(){
    1_msg := "@"
    2_msg := ","
    ;3_msg := "."

    IF Clipboard contains %1_msg%
    {
        IF Clipboard contains %2_msg%
        {
            TSLA()
        }
    }
}

WhisperCommand(){
    BlockInput On
    Send {Enter}
    Sleep 50
    Send ^v
    Send {Enter}
    BlockInput Off
    Clipboard:= ""
}

TSLA(){
    IfWinExist Path of Exile
    WinWait Path of Exile
    WinActivate Path of Exile
    WinWait Path of Exile
    {
        WhisperCommand()
    }
}
