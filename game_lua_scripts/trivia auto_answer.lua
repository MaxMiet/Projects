local ultra = "2000"
local coca = "cocacola"
local gryff = "gryffindor"
local alpha = "8"
local year = "2021"
local letter = "short"
local mammal = "giraffe"
local balloon = "balloon"
local mathone = "523"
local hunch = "quasimodo"
local wonders = "7"
local freedom = "new york"
local violin = "4"
local dice = "42"
local yes = "yes"
local best = "asgard"
local muta = "mutation"
local onetwothree = "123"
local months = "12"
local fourtwenty = "420"
local fourfive = "45"
local greek = "midas"
local batman = "gotham"
local sixtynine = "69"
onTextMessage(function(mode, text)
    if string.find(text, "premium points for ultra donation") then
        answer = ultra
        schedule(200, function() say("!answer "..answer) end)
    end
    if string.find(text, "_o_a") then
        answer = coca
        schedule(200, function() say("!answer "..answer) end)
    end
    if string.find(text, "gr_f_in") then
        answer = gryff
        schedule(200, function() say("!answer "..answer) end)
    end
    if string.find(text, "many letters in alphabet") then
        answer = alpha
        schedule(200, function() say("!answer "..answer) end)
    end
    if string.find(text, "year do we currently live") then
        answer = year
        schedule(200, function() say("!answer "..answer) end)
    end
    if string.find(text, "word becomes shorter") then
        answer = letter
        schedule(200, function() say("!answer "..answer) end)
    end
    if string.find(text, "tallest mammal") then
        answer = mammal
        schedule(200, function() say("!answer "..answer) end)
    end
    if string.find(text, "b__l") then
        answer = balloon
        schedule(200, function() say("!answer "..answer) end)
    end
    if string.find(text, "Whats 56") then
        answer = mathone
        schedule(200, function() say("!answer "..answer) end)
    end
    if string.find(text, "Hunchback") then
        answer = hunch
        schedule(200, function() say("!answer "..answer) end)
    end
    if string.find(text, "Wonders of the World") then
        answer = wonders
        schedule(200, function() say("!answer "..answer) end)
    end
    if string.find(text, "is the freedom") then
        answer = freedom
        schedule(200, function() say("!answer "..answer) end)
    end
    if string.find(text, "does a violin have") then
        answer = violin
        schedule(200, function() say("!answer "..answer) end)
    end
    if string.find(text, "pair of dice") then
        answer = dice
        schedule(200, function() say("!answer "..answer) end)
    end
    if string.find(text, "do you like") then
        answer = yes
        schedule(200, function() say("!answer "..answer) end)
    end
    if string.find(text, "best tibia server") then
        answer = best
        schedule(200, function() say("!answer "..answer) end)
    end
    if string.find(text, "muta_ion") then
        answer = muta
        schedule(200, function() say("!answer "..answer) end)
    end
    if string.find(text, "123+123-123") then
        answer = onetwothree
        schedule(200, function() say("!answer "..answer) end)
    end
    if string.find(text, "many months have") then
        answer = months
        schedule(200, function() say("!answer "..answer) end)
    end
    if string.find(text, "363+57") then
        answer = fourtwenty
        schedule(200, function() say("!answer "..answer) end)
    end
    if string.find(text, "17+28") then
        answer = fourfive
        schedule(200, function() say("!answer "..answer) end)
    end
    if string.find(text, "who turned all that") then
        answer = greek
        schedule(200, function() say("!answer "..answer) end)
    end
    if string.find(text, "batman") then
        answer = batman
        schedule(200, function() say("!answer "..answer) end)
    end
    if string.find(text, "33+36") then
        answer = sixtynine
        schedule(200, function() say("!answer "..answer) end)
    end
end)