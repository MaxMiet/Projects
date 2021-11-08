local Tranquility = say("Tranquility of immortality")
local Delusion = say("Delusion Orb")
local Elemental = usewith(3149, g_game.getAttackingCreature())
local SD = usewith(3194, g_game.getAttackingCreature())

hotkey("f8", "Combo key", function()
    if g_game.isAttacking() then 
        schedule(100, function() say("Tranquility of immortality") end)
        schedule(300, function() say("Delusion Orb") end)
        if manapercent() > 50 then
        schedule(500, function() usewith(3149, g_game.getAttackingCreature()) end)
        schedule(600, function() usewith(3194, g_game.getAttackingCreature()) end)
        else
            schedule(500, function() usewith(3194, g_game.getAttackingCreature()) end)
        end
    end
end)