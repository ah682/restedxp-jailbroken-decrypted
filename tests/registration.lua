-- Exercise the installed registration code without a WoW account or client.
local rxp, locale = arg[1], arg[2]
GetLocale = function() return locale end
strlower, strupper, tremove = string.lower, string.upper, table.remove
local function unavailable() error("Account/encryption API unexpectedly called") end
BNGetInfo = unavailable
bit = {band = unavailable, bxor = unavailable}
LibStub = function(name)
    assert(name == "LibDeflate")
    return {}
end
RXPGuides = {}
local addon = {
    player = {class = "WARRIOR", race = "Human", faction = "Alliance"},
    game = "FOREVER", RXPGuides = {},
    locale = {Get = function(text) return text end},
    NewModule = function() return {} end,
}
assert(loadfile(rxp .. "/GuideLoader.lua"))("RXPGuides", addon)
for i = 3, #arg do assert(loadfile(arg[i]))() end
assert(#addon.embeddedGuides > 0, "No guides registered")
for _, guide in ipairs(addon.embeddedGuides) do
    assert(not guide.cache, "Guides must register directly, without account-bound imports")
    io.write(guide.groupOrContent, "\0")
end
