function RandomNumber(min, max)
  return min + (Ext.Utils.MonotonicTime() % max)
end

function CanFight(target_uuid, tav_uuid)
  if Osi.IsDead(target_uuid) == 1 or Osi.HasAppliedStatusOfType(target_uuid, "INCAPACITATED") == 1 then
    return false
  end
  return Osi.IsAlly(target_uuid, tav_uuid)
end

function SendEveryoneToCamp(tav_uuid)
  -- Astarion
  if Osi.IsPartyMember("c7c13742-bacd-460a-8f65-f864fe41f255", 1) == 1 and CanFight("c7c13742-bacd-460a-8f65-f864fe41f255", tav_uuid) == 1 then
    Osi.PROC_GLO_PartyMembers_Remove("c7c13742-bacd-460a-8f65-f864fe41f255", 1)
  end
  -- Gale
  if Osi.IsPartyMember("ad9af97d-75da-406a-ae13-7071c563f604", 1) == 1 and CanFight("ad9af97d-75da-406a-ae13-7071c563f604", tav_uuid) == 1 then
    Osi.PROC_GLO_PartyMembers_Remove("ad9af97d-75da-406a-ae13-7071c563f604", 1)
  end
  -- Karlach
  if Osi.IsPartyMember("2c76687d-93a2-477b-8b18-8a14b549304c", 1) == 1 and CanFight("2c76687d-93a2-477b-8b18-8a14b549304c", tav_uuid) == 1 then
    Osi.PROC_GLO_PartyMembers_Remove("2c76687d-93a2-477b-8b18-8a14b549304c", 1)
  end
  -- Lae'zel
  if Osi.IsPartyMember("58a69333-40bf-8358-1d17-fff240d7fb12", 1) == 1 and CanFight("58a69333-40bf-8358-1d17-fff240d7fb12", tav_uuid) == 1 then
    Osi.PROC_GLO_PartyMembers_Remove("58a69333-40bf-8358-1d17-fff240d7fb12", 1)
  end
  -- Shadowheart
  if Osi.IsPartyMember("3ed74f06-3c60-42dc-83f6-f034cb47c679", 1) == 1 and CanFight("3ed74f06-3c60-42dc-83f6-f034cb47c679", tav_uuid) == 1 then
    Osi.PROC_GLO_PartyMembers_Remove("3ed74f06-3c60-42dc-83f6-f034cb47c679", 1)
  end
  -- Wyll
  if Osi.IsPartyMember("c774d764-4a17-48dc-b470-32ace9ce447d", 1) == 1 and CanFight("c774d764-4a17-48dc-b470-32ace9ce447d", tav_uuid) == 1 then
    Osi.PROC_GLO_PartyMembers_Remove("c774d764-4a17-48dc-b470-32ace9ce447d", 1)
  end
  -- Halsin
  if Osi.IsPartyMember("7628bc0e-52b8-42a7-856a-13a6fd413323", 1) == 1 and CanFight("7628bc0e-52b8-42a7-856a-13a6fd413323", tav_uuid) == 1 then
    Osi.PROC_GLO_PartyMembers_Remove("7628bc0e-52b8-42a7-856a-13a6fd413323", 1)
  end
  -- Jaheira
  if Osi.IsPartyMember("91b6b200-7d00-4d62-8dc9-99e8339dfa1a", 1) == 1 and CanFight("91b6b200-7d00-4d62-8dc9-99e8339dfa1a", tav_uuid) == 1 then
    Osi.PROC_GLO_PartyMembers_Remove("91b6b200-7d00-4d62-8dc9-99e8339dfa1a", 1)
  end
  -- Minsc
  if Osi.IsPartyMember("0de603c5-42e2-4811-9dad-f652de080eba", 1) == 1 and CanFight("0de603c5-42e2-4811-9dad-f652de080eba", tav_uuid) == 1 then
    Osi.PROC_GLO_PartyMembers_Remove("0de603c5-42e2-4811-9dad-f652de080eba", 1)
  end
  -- Minthara
  if Osi.IsPartyMember("25721313-0c15-4935-8176-9f134385451b", 1) == 1 and CanFight("25721313-0c15-4935-8176-9f134385451b", tav_uuid) == 1 then
    Osi.PROC_GLO_PartyMembers_Remove("25721313-0c15-4935-8176-9f134385451b", 1)
  end
end

function IsCompanion(uuid)
  uuid = uuid:sub(-36)
  if  uuid == "3ed74f06-3c60-42dc-83f6-f034cb47c679" or
      uuid == "c7c13742-bacd-460a-8f65-f864fe41f255" or
      uuid == "ad9af97d-75da-406a-ae13-7071c563f604" or
      uuid == "2c76687d-93a2-477b-8b18-8a14b549304c" or
      uuid == "58a69333-40bf-8358-1d17-fff240d7fb12" or
      uuid == "c774d764-4a17-48dc-b470-32ace9ce447d" or
      uuid == "7628bc0e-52b8-42a7-856a-13a6fd413323" or
      uuid == "91b6b200-7d00-4d62-8dc9-99e8339dfa1a" or
      uuid == "0de603c5-42e2-4811-9dad-f652de080eba" or
      uuid == "25721313-0c15-4935-8176-9f134385451b" then
    return true
  end
  return false
end

function StartCampFightPostShadowheartBetrayal()
  local mod_vars = Ext.Vars.GetModVariables("e49a2415-9dda-48ad-84c9-0abd35686529")
  local tav_uuid = mod_vars.BetrayerUUID
  local enemy_count = 0

  if tav_uuid ~= nil then 
    if Osi.GetFlag("b437177d-ac5d-4c44-a927-9a54b7f72bd2", "c774d764-4a17-48dc-b470-32ace9ce447d") == 1 then
      -- Tav spoke to Wyll
      Osi.ClearFlag("b437177d-ac5d-4c44-a927-9a54b7f72bd2", "c774d764-4a17-48dc-b470-32ace9ce447d")

      -- This marks Tav as aggro target
      Osi.SetFlag("b482fd66-55ef-42e3-9922-347ed847c39d", tav_uuid)

      -- Send everyone to camp
      SendEveryoneToCamp(tav_uuid)

      enemy_count = enemy_count + 1
      -- if Minsc can fight, he runs to Wyll and enters the fight
      if CanFight("0de603c5-42e2-4811-9dad-f652de080eba", tav_uuid) == 1 then
        Osi.CharacterMoveTo("0de603c5-42e2-4811-9dad-f652de080eba", "c774d764-4a17-48dc-b470-32ace9ce447d", "Run", "", 1)
        Osi.SetFaction("0de603c5-42e2-4811-9dad-f652de080eba", "3d43e9cb-9b68-cd0e-2035-d231338c3e5b")
        --Osi.TeleportTo("0de603c5-42e2-4811-9dad-f652de080eba", "c774d764-4a17-48dc-b470-32ace9ce447d")
        enemy_count = enemy_count + 1
      end
      -- if Jaheira can fight, she runs to Wyll and enters the fight
      if CanFight("91b6b200-7d00-4d62-8dc9-99e8339dfa1a", tav_uuid) == 1 then
        Osi.CharacterMoveTo("91b6b200-7d00-4d62-8dc9-99e8339dfa1a", "c774d764-4a17-48dc-b470-32ace9ce447d", "Run", "", 1)
        Osi.SetFaction("91b6b200-7d00-4d62-8dc9-99e8339dfa1a", "3d43e9cb-9b68-cd0e-2035-d231338c3e5b")
        --Osi.TeleportTo("91b6b200-7d00-4d62-8dc9-99e8339dfa1a", "c774d764-4a17-48dc-b470-32ace9ce447d")
        enemy_count = enemy_count + 1
      end
      -- Aggro Wyll
      Osi.SetFaction("c774d764-4a17-48dc-b470-32ace9ce447d", "3d43e9cb-9b68-cd0e-2035-d231338c3e5b")
    elseif Osi.GetFlag("b437177d-ac5d-4c44-a927-9a54b7f72bd2", "0de603c5-42e2-4811-9dad-f652de080eba") == 1 then
      -- Tav spoke to Minsc
      Osi.ClearFlag("b437177d-ac5d-4c44-a927-9a54b7f72bd2", "0de603c5-42e2-4811-9dad-f652de080eba")

      -- This marks Tav as aggro target
      Osi.SetFlag("b482fd66-55ef-42e3-9922-347ed847c39d", tav_uuid)

      -- Send everyone to camp
      SendEveryoneToCamp(tav_uuid)

      enemy_count = enemy_count + 1
      -- if Wyll can fight, he runs to Minsc and enters the fight
      if CanFight("c774d764-4a17-48dc-b470-32ace9ce447d", tav_uuid) == 1 then
        Osi.CharacterMoveTo("c774d764-4a17-48dc-b470-32ace9ce447d", "0de603c5-42e2-4811-9dad-f652de080eba", "Run", "", 1)
        Osi.SetFaction("c774d764-4a17-48dc-b470-32ace9ce447d", "3d43e9cb-9b68-cd0e-2035-d231338c3e5b")
        --Osi.TeleportTo("c774d764-4a17-48dc-b470-32ace9ce447d", "0de603c5-42e2-4811-9dad-f652de080eba")
        enemy_count = enemy_count + 1
      end
      -- if Jaheira can fight, she runs to Minsc and enters the fight
      if CanFight("91b6b200-7d00-4d62-8dc9-99e8339dfa1a", tav_uuid) == 1 then
        Osi.CharacterMoveTo("91b6b200-7d00-4d62-8dc9-99e8339dfa1a", "0de603c5-42e2-4811-9dad-f652de080eba", "Run", "", 1)
        Osi.SetFaction("91b6b200-7d00-4d62-8dc9-99e8339dfa1a", "3d43e9cb-9b68-cd0e-2035-d231338c3e5b")
        --Osi.TeleportTo("91b6b200-7d00-4d62-8dc9-99e8339dfa1a", "0de603c5-42e2-4811-9dad-f652de080eba")
        enemy_count = enemy_count + 1
      end
      -- Aggro Minsc
      Osi.SetFaction("0de603c5-42e2-4811-9dad-f652de080eba", "3d43e9cb-9b68-cd0e-2035-d231338c3e5b")
    elseif Osi.GetFlag("b437177d-ac5d-4c44-a927-9a54b7f72bd2", "91b6b200-7d00-4d62-8dc9-99e8339dfa1a") == 1 then
      -- Tav spoke to Jaheira
      Osi.ClearFlag("b437177d-ac5d-4c44-a927-9a54b7f72bd2", "91b6b200-7d00-4d62-8dc9-99e8339dfa1a")

      -- This marks Tav as aggro target
      Osi.SetFlag("b482fd66-55ef-42e3-9922-347ed847c39d", tav_uuid)

      -- Send everyone to camp
      SendEveryoneToCamp(tav_uuid)

      enemy_count = enemy_count + 1
      -- if Wyll can fight, he runs to Jaheira and enters the fight
      if CanFight("c774d764-4a17-48dc-b470-32ace9ce447d", tav_uuid) == 1 then
        Osi.CharacterMoveTo("c774d764-4a17-48dc-b470-32ace9ce447d", "91b6b200-7d00-4d62-8dc9-99e8339dfa1a", "Run", "", 1)
        Osi.SetFaction("c774d764-4a17-48dc-b470-32ace9ce447d", "3d43e9cb-9b68-cd0e-2035-d231338c3e5b")
        --Osi.TeleportTo("c774d764-4a17-48dc-b470-32ace9ce447d", "91b6b200-7d00-4d62-8dc9-99e8339dfa1a")
        enemy_count = enemy_count + 1
      end
      -- if Minsc can fight, teleport and aggro him
      if CanFight("0de603c5-42e2-4811-9dad-f652de080eba", tav_uuid) == 1 then
        Osi.CharacterMoveTo("0de603c5-42e2-4811-9dad-f652de080eba", "91b6b200-7d00-4d62-8dc9-99e8339dfa1a", "Run", "", 1)
        Osi.SetFaction("0de603c5-42e2-4811-9dad-f652de080eba", "3d43e9cb-9b68-cd0e-2035-d231338c3e5b")
        --Osi.TeleportTo("0de603c5-42e2-4811-9dad-f652de080eba", "91b6b200-7d00-4d62-8dc9-99e8339dfa1a")
        enemy_count = enemy_count + 1
      end
      -- Aggro Jaheira
      Osi.SetFaction("91b6b200-7d00-4d62-8dc9-99e8339dfa1a", "3d43e9cb-9b68-cd0e-2035-d231338c3e5b")
    end
  end
  if enemy_count > 0 then
    mod_vars.BetrayalFightEnemyCount = enemy_count
    mod_vars.FactionBeforeBetrayalFight = Osi.GetFaction(tav_uuid)

    -- Start the fight by adding the player to PVP1 faction
    Osi.SetFaction(tav_uuid, "f828776d-c033-4e30-4de4-cfd2e196a903")
    -- Minthara joins the evil player, if she can fight
    if CanFight("25721313-0c15-4935-8176-9f134385451b", tav_uuid) then
      Osi.CharacterMoveTo("25721313-0c15-4935-8176-9f134385451b", tav_uuid, "Run", "", 1)
      Osi.SetFaction("25721313-0c15-4935-8176-9f134385451b", "f828776d-c033-4e30-4de4-cfd2e196a903")
    end
  end
end

function FinishCampFightPostShadowheartBetrayal()
  local mod_vars = Ext.Vars.GetModVariables("e49a2415-9dda-48ad-84c9-0abd35686529")
  local tav_uuid = mod_vars.BetrayerUUID
  if tav_uuid ~= nil then
    if Osi.GetFlag("b482fd66-55ef-42e3-9922-347ed847c39d", tav_uuid) == 1 then
      local enemy_count = mod_vars.BetrayalFightEnemyCount
      if enemy_count > 0 then
        enemy_count = enemy_count - 1
      end
      if enemy_count == 0 then
        Osi.ClearFlag("b482fd66-55ef-42e3-9922-347ed847c39d", tav_uuid)
        Osi.SetFaction(mod_vars.BetrayerUUID, mod_vars.FactionBeforeBetrayalFight)
        Osi.SetFaction("25721313-0c15-4935-8176-9f134385451b", "f984f683-e819-439e-af7c-48906053c20b")
        mod_vars.BetrayerUUID = nil
        mod_vars.FactionBeforeBetrayalFight = nil
      end
      mod_vars.BetrayalFightEnemyCount = enemy_count
    end
  end
end

function CheckCompanionsLeavingParty(tav_uuid)
  -- Shadowheart
  if Osi.GetFlag("76339e33-bb45-4f1b-9d43-58773590175c", "3ed74f06-3c60-42dc-83f6-f034cb47c679") == 1 then
    CompanionLeavesParty("3ed74f06-3c60-42dc-83f6-f034cb47c679", tav_uuid)
  end
  -- Astarion
  if Osi.GetFlag("76339e33-bb45-4f1b-9d43-58773590175c", "c7c13742-bacd-460a-8f65-f864fe41f255") == 1 then
    CompanionLeavesParty("c7c13742-bacd-460a-8f65-f864fe41f255", tav_uuid)
  end
  -- Gale
  if Osi.GetFlag("76339e33-bb45-4f1b-9d43-58773590175c", "ad9af97d-75da-406a-ae13-7071c563f604") == 1 then
    CompanionLeavesParty("ad9af97d-75da-406a-ae13-7071c563f604", tav_uuid)
  end
  -- Karlach
  if Osi.GetFlag("76339e33-bb45-4f1b-9d43-58773590175c", "2c76687d-93a2-477b-8b18-8a14b549304c") == 1 then
    CompanionLeavesParty("2c76687d-93a2-477b-8b18-8a14b549304c", tav_uuid)
  end
  -- Laezel
  if Osi.GetFlag("76339e33-bb45-4f1b-9d43-58773590175c", "58a69333-40bf-8358-1d17-fff240d7fb12") == 1 then
    CompanionLeavesParty("58a69333-40bf-8358-1d17-fff240d7fb12", tav_uuid)
  end
  -- Wyll
  if Osi.GetFlag("76339e33-bb45-4f1b-9d43-58773590175c", "c774d764-4a17-48dc-b470-32ace9ce447d") == 1 then
    CompanionLeavesParty("c774d764-4a17-48dc-b470-32ace9ce447d", tav_uuid)
  end
  -- Halsin
  if Osi.GetFlag("76339e33-bb45-4f1b-9d43-58773590175c", "7628bc0e-52b8-42a7-856a-13a6fd413323") == 1 then
    CompanionLeavesParty("7628bc0e-52b8-42a7-856a-13a6fd413323", tav_uuid)
  end
  -- Jaheira
  if Osi.GetFlag("76339e33-bb45-4f1b-9d43-58773590175c", "91b6b200-7d00-4d62-8dc9-99e8339dfa1a") == 1 then
    CompanionLeavesParty("91b6b200-7d00-4d62-8dc9-99e8339dfa1a", tav_uuid)
  end
  -- Minsc
  if Osi.GetFlag("76339e33-bb45-4f1b-9d43-58773590175c", "0de603c5-42e2-4811-9dad-f652de080eba") == 1 then
    CompanionLeavesParty("0de603c5-42e2-4811-9dad-f652de080eba", tav_uuid)
  end
  -- Minthara
  if Osi.GetFlag("76339e33-bb45-4f1b-9d43-58773590175c", "25721313-0c15-4935-8176-9f134385451b") == 1 then
    CompanionLeavesParty("25721313-0c15-4935-8176-9f134385451b", tav_uuid)
  end
end

function CompanionLeavesParty(companion_uuid, tav_uuid)
  Osi.ClearFlag("76339e33-bb45-4f1b-9d43-58773590175c", companion_uuid)
  Osi.DB_CompanionLeaving(companion_uuid, tav_uuid)
  Osi.PROC_Origins_CompanionLeavePermanently(companion_uuid, "CompanionLowRelation")
  Osi.PROC_ClearOriginLeavingDialogs(companion_uuid)
  Osi.PROC_DisappearOutOfSight(companion_uuid, "Walk", 1, "GLO_CompanionLeaves_LowRelation")
end

function StartShadowheartIrregularBehavior()
  local mod_vars = Ext.Vars.GetModVariables("e49a2415-9dda-48ad-84c9-0abd35686529")
  if mod_vars.ShadowheartIrreguralBehaviorAct3 ~= 1 then
    mod_vars.ShadowheartIrreguralBehaviorAct3 = 1
    Osi.PlayLoopingAnimation(
      "3ed74f06-3c60-42dc-83f6-f034cb47c679",
      "CUST_Dejected_01_Start_55dac046-b8d2-4681-906d-f263c263071c",
      "CUST_Dejected_01_Loop_487b6cb3-1ca3-4041-acba-bcac93cfcbe5",
      "CUST_Dejected_01_End_c49344c6-72ce-460a-b55c-94708983e6be",
      "CUST_Dejected_01_Loop_487b6cb3-1ca3-4041-acba-bcac93cfcbe5",
      "CUST_Dejected_01_Loop_487b6cb3-1ca3-4041-acba-bcac93cfcbe5",
      "CUST_Dejected_01_Loop_487b6cb3-1ca3-4041-acba-bcac93cfcbe5",
      "CUST_Dejected_01_Loop_487b6cb3-1ca3-4041-acba-bcac93cfcbe5")
  end
end

function GetTavUUID()
  Ext.Utils.Print("ReallyShadowheart: GetTavUUID")
  local players = Osi.DB_Players:Get(nil)
  for _, player in ipairs(players) do
    local player_uuid = player[1]:sub(-36)
    Ext.Utils.Print("ReallyShadowheart: GetTavUUID player_uuid = " .. player_uuid)
    if Osi.IsTagged(player_uuid, "306b9b05-1057-4770-aa17-01af21acd650") then
      Ext.Utils.Print("ReallyShadowheart: GetTavUUID tav_uuid = " .. player_uuid)
      return player_uuid
    end
  end
  return nil
end

Ext.Vars.RegisterModVariable("e49a2415-9dda-48ad-84c9-0abd35686529", "BetrayerUUID", {
  Server = true, Client = false, SyncToClient = false
})

Ext.Vars.RegisterModVariable("e49a2415-9dda-48ad-84c9-0abd35686529", "FactionBeforeBetrayalFight", {
  Server = true, Client = false, SyncToClient = false
})

Ext.Vars.RegisterModVariable("e49a2415-9dda-48ad-84c9-0abd35686529", "BetrayalFightEnemyCount", {
  Server = true, Client = false, SyncToClient = false
})

Ext.Vars.RegisterModVariable("e49a2415-9dda-48ad-84c9-0abd35686529", "ShadowheartIrreguralBehaviorAct3", {
  Server = true, Client = false, SyncToClient = false
})

Ext.Vars.RegisterModVariable("e49a2415-9dda-48ad-84c9-0abd35686529", "ShadowheartParentsPointsCounter", {
  Server = true, Client = false, SyncToClient = false
})

Ext.Osiris.RegisterListener("FlagSet", 3, "after", function(flag, speaker, instanceId)
  local flag_uuid = flag:sub(-36)
  local speaker_uuid = speaker:sub(-36)
  local Shadowheart_UUID = "3ed74f06-3c60-42dc-83f6-f034cb47c679"
  local Astarion_UUID = "c7c13742-bacd-460a-8f65-f864fe41f255"
  local Gale_UUID = "ad9af97d-75da-406a-ae13-7071c563f604"
  local Karlach_UUID = "2c76687d-93a2-477b-8b18-8a14b549304c"
  local Laezel_UUID = "58a69333-40bf-8358-1d17-fff240d7fb12"
  local Wyll_UUID = "c774d764-4a17-48dc-b470-32ace9ce447d"
  local Halsin_UUID = "7628bc0e-52b8-42a7-856a-13a6fd413323"
  local Jaheira_UUID = "91b6b200-7d00-4d62-8dc9-99e8339dfa1a"
  local Minsc_UUID = "0de603c5-42e2-4811-9dad-f652de080eba"
  local Minthara_UUID = "25721313-0c15-4935-8176-9f134385451b"

  --Ext.Utils.Print("Flag " .. flag_uuid .. " was set on " .. speaker_uuid)

  if flag_uuid == "f6bff638-5de1-4ac5-9e6f-c2c61206f952" then
    Osi.ChangeApprovalRating(Shadowheart_UUID, speaker_uuid, 0, -10)
    Ext.Utils.Print("Reduced Shadowheart's approval of Tav by 10")
  elseif flag_uuid == "add81fd0-0641-45d3-8020-29098ccc22d7" then
    local current_approval = Osi.GetApprovalRating(Shadowheart_UUID, speaker_uuid)
    Ext.Utils.Print("Current approval = " .. current_approval .. "; speaker uuid = " .. speaker_uuid)
    if current_approval > 0 then
      local approval_change = 0 - current_approval
      Osi.ChangeApprovalRating(Shadowheart_UUID, speaker_uuid, 0, approval_change)
      Ext.Utils.Print("Set approval to ZERO, speaker uuid: " .. speaker_uuid)
    end
  elseif flag_uuid == "a562c158-cb0c-40a9-9f34-44f76bfdfbf6" then
    local current_approval = Osi.GetApprovalRating(Shadowheart_UUID, speaker_uuid)
    Ext.Utils.Print("Current approval = " .. current_approval .. "; speaker uuid = " .. speaker_uuid)
    if current_approval > 35 then
      local approval_change = 35 - current_approval
      Osi.ChangeApprovalRating(Shadowheart_UUID, speaker_uuid, 0, approval_change)
      Ext.Utils.Print("Set approval to 35, speaker uuid: " .. speaker_uuid)
    end
  elseif flag_uuid == "42a1da52-ccf5-46a0-954d-8f1c53dd20b6" then
    local current_approval = Osi.GetApprovalRating(Shadowheart_UUID, speaker_uuid)
    Ext.Utils.Print("Current approval = " .. current_approval .. "; speaker uuid = " .. speaker_uuid)
    if current_approval > -19 then
      local approval_change = 0 - current_approval - 19
      Osi.ChangeApprovalRating(Shadowheart_UUID, speaker_uuid, 0, approval_change)
      Ext.Utils.Print("Set approval to NEUTRAL, speaker uuid: " .. speaker_uuid)
    end
  elseif flag_uuid == "2701e07a-73a2-4b96-9951-9080555f3f8f" then
    local current_approval = Osi.GetApprovalRating(Shadowheart_UUID, speaker_uuid)
    Ext.Utils.Print("Current approval = " .. current_approval .. "; speaker uuid = " .. speaker_uuid)
    if current_approval > -25 then
      local approval_change = 0 - current_approval - 25
      Osi.ChangeApprovalRating(Shadowheart_UUID, speaker_uuid, 0, approval_change)
      Ext.Utils.Print("Set approval to LOW, speaker uuid: " .. speaker_uuid)
    end
  elseif flag_uuid == "c80bad74-7669-4989-a912-106fd2ed4cd9" then
    local current_approval = Osi.GetApprovalRating(Shadowheart_UUID, speaker_uuid)
    Ext.Utils.Print("Current approval = " .. current_approval .. "; speaker uuid = " .. speaker_uuid)
    if current_approval > -40 then
      local approval_change = 0 - current_approval - 40
      Osi.ChangeApprovalRating(Shadowheart_UUID, speaker_uuid, 0, approval_change)
      Ext.Utils.Print("Set approval to VERY LOW, speaker uuid: " .. speaker_uuid)
    end
  elseif flag_uuid == "d20cc281-6ed6-4e9b-bad5-28d403a2b0af" then
    local effect_resource = "EFFECTRESOURCEGUID_VFX_UI_ExclamationMark_01_a3018cf0-3a25-06ee-206a-3dd079332d80"
    local effect_tag = "Shadowheart_breakup"
    Osi.PROC_LoopEffect(effect_resource, Shadowheart_UUID, effect_tag, "__ANY__", "Dummy_OverheadFX");
  elseif flag_uuid == "80a1a14e-f831-4b3f-815a-684dc15f77e7" then
    local effect_tag = "Shadowheart_breakup"
    local effect_resource = "EFFECTRESOURCEGUID_VFX_UI_ExclamationMark_01_a3018cf0-3a25-06ee-206a-3dd079332d80"
    local rows = Osi.DB_LoopEffect:Get(Shadowheart_UUID, nil, effect_tag, nil, effect_resource, nil, nil)
    for k, v in pairs(rows) do
      local loop_effect_handle = v[2]
      Osi.StopLoopEffect(loop_effect_handle)
    end
    Osi.DB_LoopEffect:Delete(Shadowheart_UUID, nil, effect_tag, nil, effect_resource, nil, nil)
  elseif flag_uuid == "fb53edc2-9a89-4ad2-af83-20b5fe425cdd" then
    if Osi.GetFlag("161b7223-039d-4ebe-986f-1dcd9a66733f", Shadowheart_UUID) then
      Ext.Utils.Print("ReallyShadowheart: Night time in Camp")

      -- Clear ORI_ShadowheartAnotherSwimmingLessonReplied
      Osi.ClearFlag("8942cfa4-550f-482b-8b27-56625dee1c15", Shadowheart_UUID)

      local tav_uuid = GetTavUUID()
      if tav_uuid == nil then
        Ext.Utils.Print("ReallyShadowheart: tav UUID is nil")
        return
      end
      if Osi.GetFlag("2774e4ec-e92d-41c1-a4b0-c6ddc84417da", tav_uuid) == 1 and Osi.GetFlag("c8f7b189-ea19-4a74-b581-305abdc9eb19", tav_uuid) == 0 then
        Osi.PROC_RelationshipDialog(
          "3ed74f06-3c60-42dc-83f6-f034cb47c679",
          "95ca3833-09d0-5772-b16a-c7a5e9208fe5",
          "2774e4ec-e92d-41c1-a4b0-c6ddc84417da",
          "3ed74f06-3c60-42dc-83f6-f034cb47c679", 0)
      end
    end
  elseif flag_uuid == "46190b70-0be5-4f11-834c-59b278211de2" then
    Osi.DB_CampNight_RomanceNight(
      "NIGHT_Shadowheart_Skinnydipping_9f583304-0a1a-498c-acf9-3c8dcc30ee3d",
      "S_Player_ShadowHeart_3ed74f06-3c60-42dc-83f6-f034cb47c679",
      "CAMP_Shadowheart_SkinnyDipping_SD_ROM_700d677f-1bfd-1c83-8530-0db12875c33b",
      "ORI_Shadowheart_Event_SkinnyDippingRomanceScene_3437a073-b92a-4999-b6b9-e7745865a0c2")
    Osi.DB_Camp_QueuedNight("NIGHT_Shadowheart_Skinnydipping_9f583304-0a1a-498c-acf9-3c8dcc30ee3d")
    Osi.ClearFlag("46190b70-0be5-4f11-834c-59b278211de2", Shadowheart_UUID)
  elseif flag_uuid == "7495e78c-9e70-4ea9-95eb-17fde7f94b7c" then
    local n = RandomNumber(1, 6)
    Ext.Utils.Print("Kiss " .. n .. " is selected")
    Osi.ClearFlag("f2781286-e51c-443f-b1a3-cea4ba95ccf9", Shadowheart_UUID)
    Osi.ClearFlag("815a0406-7c85-4107-b704-439320fb7f0b", Shadowheart_UUID)
    Osi.ClearFlag("c07bfea6-3d37-48f3-aefc-6eb1749b117f", Shadowheart_UUID)
    Osi.ClearFlag("db362653-5649-4f1d-bc43-32b85fd42c0e", Shadowheart_UUID)
    Osi.ClearFlag("ec79178f-2c18-4a71-b147-7b254439e5b2", Shadowheart_UUID)
    Osi.ClearFlag("321d447c-5298-4a5c-82de-f884ba4757d4", Shadowheart_UUID)
    Osi.ClearFlag("7495e78c-9e70-4ea9-95eb-17fde7f94b7c", Shadowheart_UUID)
    if n == 1 then
      Osi.SetFlag("f2781286-e51c-443f-b1a3-cea4ba95ccf9", Shadowheart_UUID)
    elseif n == 2 then
      Osi.SetFlag("815a0406-7c85-4107-b704-439320fb7f0b", Shadowheart_UUID)
    elseif n == 3 then
      Osi.SetFlag("c07bfea6-3d37-48f3-aefc-6eb1749b117f", Shadowheart_UUID)
    elseif n == 4 then
      Osi.SetFlag("db362653-5649-4f1d-bc43-32b85fd42c0e", Shadowheart_UUID)
    elseif n == 5 then
      Osi.SetFlag("ec79178f-2c18-4a71-b147-7b254439e5b2", Shadowheart_UUID)
    else
      Osi.SetFlag("321d447c-5298-4a5c-82de-f884ba4757d4", Shadowheart_UUID)
    end
  elseif flag_uuid == "550ff254-7218-4e11-9699-17d837da43f8" then
    Osi.MoveAllLootableItemsTo('b1ea974d-96fb-47ca-b6d9-9c85fcb69313', speaker_uuid, 1, 1, 1, 0)
  elseif flag_uuid == "1b4b377c-10c2-45eb-a475-6b4944995fbf" then
    Ext.Utils.Print("ReallyShadowheart: Companions are gonna kick player's ass, target uuid = " .. speaker_uuid)
    local mod_vars = Ext.Vars.GetModVariables("e49a2415-9dda-48ad-84c9-0abd35686529")
    mod_vars.BetrayerUUID = speaker_uuid
  elseif flag_uuid == "161b7223-039d-4ebe-986f-1dcd9a66733f" and speaker_uuid == Shadowheart_UUID then
    if  Osi.GetFlag("6f8e2b2b-5ffa-4e83-adf7-d80a8e36a8d8", Shadowheart_UUID) == 1 and
        Osi.GetFlag("4777f4c8-d5ee-4d4e-83cc-243b3c837fa8", Shadowheart_UUID) ~= 1 then
      StartShadowheartIrregularBehavior()
    end
  elseif flag_uuid == '4777f4c8-d5ee-4d4e-83cc-243b3c837fa8' and speaker_uuid == Shadowheart_UUID then
    Osi.PlayAnimation("3ed74f06-3c60-42dc-83f6-f034cb47c679", "CUST_Dejected_01_End_c49344c6-72ce-460a-b55c-94708983e6be")
  elseif flag_uuid == "414f6e7d-4a86-4cdf-b5aa-31d053ae76d9" then
    -- This sets FLAG_ORI_Shadowheart_ShadowheartBetrayed on all companions
    Osi.SetFlag("f78e829a-55cb-4dbf-859e-2f125471fbdc", Astarion_UUID)
    Osi.SetFlag("f78e829a-55cb-4dbf-859e-2f125471fbdc", Gale_UUID)
    Osi.SetFlag("f78e829a-55cb-4dbf-859e-2f125471fbdc", Karlach_UUID)
    Osi.SetFlag("f78e829a-55cb-4dbf-859e-2f125471fbdc", Laezel_UUID)
    Osi.SetFlag("f78e829a-55cb-4dbf-859e-2f125471fbdc", Wyll_UUID)
    Osi.SetFlag("f78e829a-55cb-4dbf-859e-2f125471fbdc", Minthara_UUID)
    Osi.SetFlag("8069e1a8-51b5-afc0-de8c-f5af844f034d", Minthara_UUID)
    Osi.SetFlag("f78e829a-55cb-4dbf-859e-2f125471fbdc", Minsc_UUID)
    Osi.SetFlag("f78e829a-55cb-4dbf-859e-2f125471fbdc", Jaheira_UUID)
    Osi.SetFlag("f78e829a-55cb-4dbf-859e-2f125471fbdc", Halsin_UUID)
  elseif flag_uuid == '600ca39c-5887-4657-bf4c-d417cc3d146b' or flag_uuid == 'a1cf2f2f-8f3f-4ac7-a1f7-32e3bdb1bda4' or flag_uuid == '56084254-ec74-4c13-8eb2-6e8163f16b8f' then
    local mod_vars = Ext.Vars.GetModVariables("e49a2415-9dda-48ad-84c9-0abd35686529")
    --Ext.Utils.Print("ReallyShadowheart: memorable location at Baldur's Gate")
    if mod_vars.ShadowheartParentsPointsCounter == 1 then
      --Ext.Utils.Print("ReallyShadowheart: visited 2 memorable locations or more")
      Osi.SetFlag("ac830dd2-bad2-44aa-9970-136c16477500", Shadowheart_UUID)
      Osi.SetFlag("c5c03e5f-44af-4347-a081-bbbd9d5fc632", Shadowheart_UUID)
      Osi.PROC_RelationshipDialog(
        "3ed74f06-3c60-42dc-83f6-f034cb47c679",
        "95ca3833-09d0-5772-b16a-c7a5e9208fe5",
        "c5c03e5f-44af-4347-a081-bbbd9d5fc632",
        "3ed74f06-3c60-42dc-83f6-f034cb47c679", 0)
    else
      mod_vars.ShadowheartParentsPointsCounter = 1
    end
  end
end)

--Ext.Osiris.RegisterListener("StatusApplied", 4, "before", function(object, status, causee, storyActionID)
--  Ext.Utils.Print("ReallyShadowheart: StatusApplied")
--  if object ~= nil then
--    Ext.Utils.Print("ReallyShadowheart: StatusApplied object = " .. object)
--  else
--    Ext.Utils.Print("ReallyShadowheart: StatusApplied object is nil")
--  end
--  if status ~= nil then
--    Ext.Utils.Print("ReallyShadowheart: StatusApplied status = " .. status)
--  else
--    Ext.Utils.Print("ReallyShadowheart: StatusApplied status is nil")
--  end
--  if causee ~= nil then
--    Ext.Utils.Print("ReallyShadowheart: StatusApplied causee = " .. causee)
--  else
--    Ext.Utils.Print("ReallyShadowheart: StatusApplied causee is nil")
--  end
--  if storyActionID ~= nil then
--    Ext.Utils.Print("ReallyShadowheart: StatusApplied storyActionID = " .. storyActionID)
--  else
--    Ext.Utils.Print("ReallyShadowheart: StatusApplied storyActionID is nil")
--  end
--end)

--Ext.Osiris.RegisterListener("PROC_LongRest", 0, "before", function()
--  Ext.Utils.Print("ReallyShadowheart: LONG REST (before)")
--
  -- Reset ORI_Shadowheart_AfterParents
--  Osi.ClearFlag("6f8e2b2b-5ffa-4e83-adf7-d80a8e36a8d8", "3ed74f06-3c60-42dc-83f6-f034cb47c679")
--
  -- Reset ORI_ShadowheartAnotherSwimmingLessonReplied 
--  Osi.ClearFlag("8942cfa4-550f-482b-8b27-56625dee1c15", "3ed74f06-3c60-42dc-83f6-f034cb47c679")
--
  -- Check if ORI_ShadowheartMoreOpportunitiesToSlipAway is set, and set ORI_LongRestBeforeMoreOpportunitiesToSlipAway on long rest
  -- This prevents the "more opportunities to slip away" option from appearing immediately after the post-skinny dipping conversation
--  if Osi.GetFlag("2f2779cf-4a7b-44ef-8458-d29b48578740", "3ed74f06-3c60-42dc-83f6-f034cb47c679") then
--    Osi.SetFlag("fec1c849-c9b6-47ab-9dd4-84acff4cd01a", "3ed74f06-3c60-42dc-83f6-f034cb47c679")
--  end
--end) DB_CAMP_SkipSleepCutscene

--Ext.Osiris.RegisterListener("PROC_Camp_PlacePlayerInBed", 2, "after", function(character, bed)
--  Ext.Utils.Print("ReallyShadowheart: PROC_Camp_PlacePlayerInBed " .. character .. " to bed " .. bed)
--end)

--Ext.Osiris.RegisterListener("StatusApplied", 4, "before", function(object, status, cause, action_id)
--  if object == "S_Player_ShadowHeart_3ed74f06-3c60-42dc-83f6-f034cb47c679" then
--    Ext.Utils.Print("ReallyShadowheart: StatusApplied " .. object .. ", " .. status .. ", " .. cause)
--  end
--end)

--Ext.Osiris.RegisterListener("StatusRemoved", 4, "before", function(object, status, cause, action_id)
--  if object == "S_Player_ShadowHeart_3ed74f06-3c60-42dc-83f6-f034cb47c679" then
--    Ext.Utils.Print("ReallyShadowheart: StatusRemoved " .. object .. ", " .. status .. ", " .. cause)
--  end
--end)

function GetDBQueryResult(result)
  if result == nil then
    return nil
  end
  result = result[1]
  if result == nil then
    return nil
  end
  result = result[1]
  return result
end

Ext.Osiris.RegisterListener("LongRestStarted", 0, "before", function()
  Ext.Utils.Print("ReallyShadowheart: LongRestStarted")
  local tav_uuid = Osi.GetHostCharacter()
  if tav_uuid == nil then
    Ext.Utils.Print("ReallyShadowheart: LongRestStarted, Tav uuid is nil")
    return
  end
  local random_number = Osi.Random(2)
  if random_number == 1 then
    Osi.SetFlag("eff18d52-34d0-4578-8891-eb8e6bfdbf32", tav_uuid)
    Ext.Utils.Print("ReallyShadowheart: alternative night sleep cutscene")
  else
    Osi.ClearFlag("eff18d52-34d0-4578-8891-eb8e6bfdbf32", tav_uuid)
    Ext.Utils.Print("ReallyShadowheart: default night sleep cutscene")
  end
end)


Ext.Osiris.RegisterListener("LongRestFinished", 0, "after", function()
  Ext.Utils.Print("ReallyShadowheart: LongRestFinished")

  -- Reset ORI_Shadowheart_AfterParents
  Osi.ClearFlag("6f8e2b2b-5ffa-4e83-adf7-d80a8e36a8d8", "3ed74f06-3c60-42dc-83f6-f034cb47c679")

  -- Reset ORI_ShadowheartAnotherSwimmingLessonReplied 
  Osi.ClearFlag("8942cfa4-550f-482b-8b27-56625dee1c15", "3ed74f06-3c60-42dc-83f6-f034cb47c679")

  -- Reset Shadowheart_Hesitated_To_Ask
  Osi.ClearFlag("d8d602d9-d2ab-4a8e-8ffb-c465fd52ce18", "3ed74f06-3c60-42dc-83f6-f034cb47c679")

  -- Reset Tav_Said_Love_You
  Osi.ClearFlag("ea47a913-77a8-4a7e-bdfb-a13880f25107", "3ed74f06-3c60-42dc-83f6-f034cb47c679")

  -- Reset Tav_Already_Prayed_With_Her_Today
  Osi.ClearFlag("a2a96abb-1b40-42fe-9f8b-6685eb173c63", "3ed74f06-3c60-42dc-83f6-f034cb47c679")

  -- Check if ORI_ShadowheartMoreOpportunitiesToSlipAway is set, and set ORI_LongRestBeforeMoreOpportunitiesToSlipAway on long rest
  -- This prevents the "more opportunities to slip away" option from appearing immediately after the post-skinny dipping conversation
  if Osi.GetFlag("2f2779cf-4a7b-44ef-8458-d29b48578740", "3ed74f06-3c60-42dc-83f6-f034cb47c679") then
    Osi.SetFlag("fec1c849-c9b6-47ab-9dd4-84acff4cd01a", "3ed74f06-3c60-42dc-83f6-f034cb47c679")
  end
end)

Ext.Osiris.RegisterListener("ApprovalRatingChanged", 3, "after", function(rating_owner, rated_character, new_approval)
  Ext.Utils.Print("ApprovalRatingChanged " .. rating_owner .. ", " .. rated_character .. ", " .. new_approval)
  if rating_owner == "3ed74f06-3c60-42dc-83f6-f034cb47c679" then
    Osi.SetFlag("5f660cf8-4824-4930-a3f7-cc384c40c786", rated_character)
    if new_approval >= 80 then
      Ext.Utils.Print("Shadowheart approval >= 80")
      Osi.SetFlag("f1391075-7de2-450e-aac3-c33ff6b3d1dd", rated_character)
    else
      Ext.Utils.Print("Shadowheart approval < 80")
      Osi.ClearFlag("f1391075-7de2-450e-aac3-c33ff6b3d1dd", rated_character)
    end
  end
end)

Ext.Osiris.RegisterListener("DialogStarted", 2, "after", function(dialog_resource, dialog_id)
  Ext.Utils.Print("DialogStarted " .. dialog_resource .. ", " .. dialog_id)
--  local speaker1 = Osi.DialogGetInvolvedPlayer(dialog_id, 1)
--  local speaker2 = Osi.DialogGetInvolvedPlayer(dialog_id, 2)
--  local speaker3 = Osi.DialogGetInvolvedPlayer(dialog_id, 3)
--  local speaker4 = Osi.DialogGetInvolvedPlayer(dialog_id, 4)
--  if speaker1 ~= nil then
--    Ext.Utils.Print("DialogStarted, speaker 1: " .. speaker1)
--  else
--    Ext.Utils.Print("DialogStarted, speaker 1: nil")
--  end
--  if speaker2 ~= nil then
--    Ext.Utils.Print("DialogStarted, speaker 2: " .. speaker2)
--  else
--    Ext.Utils.Print("DialogStarted, speaker 2: nil")
--  end
--  if speaker3 ~= nil then
--    Ext.Utils.Print("DialogStarted, speaker 3: " .. speaker3)
--  else
--    Ext.Utils.Print("DialogStarted, speaker 3: nil")
--  end
--  if speaker4 ~= nil then
--    Ext.Utils.Print("DialogStarted, speaker 4: " .. speaker4)
--  else
--    Ext.Utils.Print("DialogStarted, speaker 4: nil")
--  end
end)

Ext.Osiris.RegisterListener("DialogEnded", 2, "after", function(dialog_resource, dialog_id)
  Ext.Utils.Print("DialogEnded " .. dialog_resource .. ", " .. dialog_id)
  local tav_uuid = Osi.GetHostCharacter()
  if tav_uuid ~= nil then
    CheckCompanionsLeavingParty(tav_uuid)
  end
  Ext.OnNextTick(function()
    StartCampFightPostShadowheartBetrayal()
  end)
end)


Ext.Osiris.RegisterListener("DB_Dead", 1, "after", function(who)
  local faction = Osi.GetFaction(who)
  if faction ~= nil and IsCompanion(who) then
    faction = faction:sub(-36)
    if faction == "3d43e9cb-9b68-cd0e-2035-d231338c3e5b" then
      FinishCampFightPostShadowheartBetrayal()
    end
  end
end)

Ext.Osiris.RegisterListener("VoiceBarkEnded", 2, "after", function(bark_id, instance_id)
--  Ext.Utils.Print("ReallyShadowheart: VoiceBarkEnded " .. bark_id)
  local bark_uuid = bark_id:sub(-36)
  if bark_uuid == "62043e30-4a81-62e2-c9db-ea950ce747de" then
    Osi.PROC_RelationshipDialog(
      "S_Player_ShadowHeart_3ed74f06-3c60-42dc-83f6-f034cb47c679",
      "ShadowHeart_InParty_95ca3833-09d0-5772-b16a-c7a5e9208fe5",
      "S_Player_ShadowHeart_3ed74f06-3c60-42dc-83f6-f034cb47c679");
  end
end)



Ext.Utils.Print("")
Ext.Utils.Print("  .--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--. ")
Ext.Utils.Print(" / .. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\")
Ext.Utils.Print(" \\ \\/\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ \\/ /")
Ext.Utils.Print("  \\/ /`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'\\/ / ")
Ext.Utils.Print("  / /\\                                                                                                    / /\\ ")
Ext.Utils.Print(" / /\\ \\   ____            _ _         ____  _               _               _                     _      / /\\ \\")
Ext.Utils.Print(" \\ \\/ /  |  _ \\ ___  __ _| | |_   _  / ___|| |__   __ _  __| | _____      _| |__   ___  __ _ _ __| |_    \\ \\/ /")
Ext.Utils.Print("  \\/ /   | |_) / _ \\/ _` | | | | | | \\___ \\| '_ \\ / _` |/ _` |/ _ \\ \\ /\\ / / '_ \\ / _ \\/ _` | '__| __|    \\/ / ")
Ext.Utils.Print("  / /\\   |  _ <  __/ (_| | | | |_| |  ___) | | | | (_| | (_| | (_) \\ V  V /| | | |  __/ (_| | |  | |_     / /\\ ")
Ext.Utils.Print(" / /\\ \\  |_| \\_\\___|\\__,_|_|_|\\__, | |____/|_| |_|\\__,_|\\__,_|\\___/ \\_/\\_/ |_| |_|\\___|\\__,_|_|   \\__|   / /\\ \\")
Ext.Utils.Print(" \\ \\/ /                       |___/                                                                      \\ \\/ /")
Ext.Utils.Print("  \\/ /                                                                                                    \\/ / ")
Ext.Utils.Print("  / /\\.--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--./ /\\ ")
Ext.Utils.Print(" / /\\ \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\/\\ \\")
Ext.Utils.Print(" \\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `' /")
Ext.Utils.Print("  `--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--' ")
Ext.Utils.Print("")
