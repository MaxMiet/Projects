local tChannel= getChannelId("Help")
local find_msg = ":" -- lower case
onTalk(function(name, level, mode, text, channelId, pos)
    if channelId == tChannel then
        playSound("/sounds/magnum.ogg")
    end
end)

local pChannel= getChannelId("Admin")
local find_msg = ":" -- lower case
onTalk(function(name, level, mode, text, channelId, pos)
    if channelId == pChannel then
        playSound("/sounds/magnum.ogg")
    end
end)