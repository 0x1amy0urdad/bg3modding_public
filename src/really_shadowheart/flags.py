from __future__ import annotations

import bg3moddinglib as bg3

from .context import files


#################
# Custom flags
#################

# Mod health check

Osiris_Health_Check = bg3.flag_object(
    files, 'Osiris_Health_Check', bg3.OBJECT_FLAG, flag_uuid='dd83b1a1-2fa2-4ef7-a104-8c2471da6d50', description='Osiris health check')

Osiris_Health_Check_Passed = bg3.flag_object(
    files, 'Osiris_Health_Check_Passed', bg3.OBJECT_FLAG, flag_uuid='1f2366eb-73ce-4e39-bbd8-cb0684870b34', description='Osiris health check passed')

ScriptExtender_Health_Check = bg3.flag_object(
    files, 'ScriptExtender_Health_Check', bg3.OBJECT_FLAG, flag_uuid='0ba4d9cb-316e-4c14-b6c7-fb98cafe3ad3', description='Script Extender health check')

ScriptExtender_Health_Check_Passed = bg3.flag_object(
    files, 'ScriptExtender_Health_Check_Passed', bg3.OBJECT_FLAG, flag_uuid='29d042a5-e1a4-4791-95a6-b3ef5e7f5a28', description='Script Extender health check passed')


# Kisses
ORI_ShadowheartKiss_StartRandom = bg3.flag_object(
    files, 'ORI_ShadowheartKiss_StartRandom', bg3.OBJECT_FLAG, flag_uuid='7495e78c-9e70-4ea9-95eb-17fde7f94b7c', description='Shadowheart random kiss start')
ORI_ShadowheartKiss_VersionA = bg3.flag_object(
    files, 'ORI_ShadowheartKiss_VersionA', bg3.OBJECT_FLAG, flag_uuid='f2781286-e51c-443f-b1a3-cea4ba95ccf9', description='Shadowheart kiss variant A')
ORI_ShadowheartKiss_VersionB = bg3.flag_object(
    files, 'ORI_ShadowheartKiss_VersionB', bg3.OBJECT_FLAG, flag_uuid='815a0406-7c85-4107-b704-439320fb7f0b', description='Shadowheart kiss variant B')
ORI_ShadowheartKiss_VersionC = bg3.flag_object(
    files, 'ORI_ShadowheartKiss_VersionC', bg3.OBJECT_FLAG, flag_uuid='c07bfea6-3d37-48f3-aefc-6eb1749b117f', description='Shadowheart kiss variant C')
ORI_ShadowheartKiss_VersionD = bg3.flag_object(
    files, 'ORI_ShadowheartKiss_VersionD', bg3.OBJECT_FLAG, flag_uuid='db362653-5649-4f1d-bc43-32b85fd42c0e', description='Shadowheart kiss variant D')
ORI_ShadowheartKiss_VersionE = bg3.flag_object(
    files, 'ORI_ShadowheartKiss_VersionE', bg3.OBJECT_FLAG, flag_uuid='ec79178f-2c18-4a71-b147-7b254439e5b2', description='Shadowheart kiss variant E')
ORI_ShadowheartKiss_VersionF = bg3.flag_object(
    files, 'ORI_ShadowheartKiss_VersionF', bg3.OBJECT_FLAG, flag_uuid='321d447c-5298-4a5c-82de-f884ba4757d4', description='Shadowheart kiss variant F')
ORI_ShadowheartKiss_LoveYou = bg3.flag_object(
    files, 'ORI_ShadowheartKiss_LoveYou', bg3.OBJECT_FLAG, flag_uuid='9e69e807-7153-45ab-8821-c5ece0716df7', description='Shadowheart kiss love you')

# Under construction flag
Under_Construction = bg3.flag_object(
    files, 'Under_Construction', bg3.OBJECT_FLAG, flag_uuid='63ffe70f-4ad7-498c-966e-a47106e3b23d', description='Set to true to show unfinished content')

# Shadowheart_Shadow_Cursed
Shadowheart_Shadow_Cursed = bg3.flag_object(
    files, 'Shadowheart_Shadow_Cursed', bg3.OBJECT_FLAG, flag_uuid='a2a44d74-eb8d-4d22-bc14-ddf9d482aed9', description='Shar didnt protect Shadowheart from the Shadow Curse')

# Shadowheart_Shadow_Cursed_Event
Shadowheart_Shadow_Cursed_Event = bg3.flag_object(
    files, 'Shadowheart_Shadow_Cursed_Event', bg3.OBJECT_FLAG, flag_uuid='e1f3e587-9872-4735-9169-c5df785a634d', description='Trigger flag for the new faith discussion')


# Shadowheart needs a night to get her thoughts together
Shadowheart_After_Parents_Crisis = bg3.flag_object(
    files, 'Shadowheart_After_Parents_Crisis', bg3.OBJECT_FLAG, flag_uuid='6f8e2b2b-5ffa-4e83-adf7-d80a8e36a8d8', description='Shadowheart needs a night to get her thoughts together')

# Shadowheart cried and got her thoughts together
Shadowheart_Cried_After_Parents = bg3.flag_object(
    files, 'Shadowheart_Cried_After_Parents', bg3.OBJECT_FLAG, flag_uuid='4777f4c8-d5ee-4d4e-83cc-243b3c837fa8', description='Shadowheart cried and got her thoughts together')

# Loot_Viconias_Stuff flag
Loot_Viconias_Stuff = bg3.flag_object(
    files, 'Loot_Viconias_Stuff', bg3.OBJECT_FLAG, flag_uuid='550ff254-7218-4e11-9699-17d837da43f8', description="Loot Viconia's stuff")

# Shadowheart_State_Smiles_When_Hugged
Shadowheart_State_Smiles_When_Hugged = bg3.flag_object(
    files, 'Shadowheart_State_Smiles_When_Hugged', bg3.OBJECT_FLAG, flag_uuid='3486a7e3-97c8-464b-9afa-665e8ec981ff', description='Shadowheart is hugged and she smiles')

# Shadowheart_State_Hugs_Enabled flag
Shadowheart_State_Hugs_Enabled = bg3.flag_object(
    files, 'Shadowheart_State_Hugs_Enabled', bg3.OBJECT_FLAG, flag_uuid='9402335a-e23e-464b-9c18-fb5fed9eff04', description='Shadowheart was hugged, she liked that and wants more hugs')

# Shadowheart_State_Hug_Reaction
Shadowheart_State_Hug_Reaction = bg3.flag_object(
    files, 'Shadowheart_State_Hug_Reaction', bg3.OBJECT_FLAG, flag_uuid='b55cf115-9659-4b46-9150-ae4a261ea0af', description='Shadowheart reacts to the first hug when she is not sad')

# Shadowheart_More_Opportunities_To_Slip_Away flag
Shadowheart_More_Opportunities_To_Slip_Away = bg3.flag_object(
    files, 'Shadowheart_More_Opportunities_To_Slip_Away', bg3.OBJECT_FLAG, flag_uuid='2f2779cf-4a7b-44ef-8458-d29b48578740', description='Shadowheart says that she hopes for more opportunities to slip away')

# Shadowheart_LongRest_Before_More_Opportunities_To_Slip_Away flag
Shadowheart_LongRest_Before_More_Opportunities_To_Slip_Away = bg3.flag_object(
    files, 'Shadowheart_LongRest_Before_More_Opportunities_To_Slip_Away', bg3.OBJECT_FLAG, flag_uuid='fec1c849-c9b6-47ab-9dd4-84acff4cd01a', description='Wait 1 long rest before asking Shadowheart to slip away again')

# Shadowheart_Another_Swimming_Lesson_Replied flag
Shadowheart_Another_Swimming_Lesson_Replied = bg3.flag_object(
    files, 'Shadowheart_Another_Swimming_Lesson_Replied', bg3.OBJECT_FLAG, flag_uuid='8942cfa4-550f-482b-8b27-56625dee1c15', description='Shadowheart replied to a proposal of seizing an opportunity')

# Shadowheart_AnotherSwimmingLesson flag
Shadowheart_AnotherSwimmingLesson = bg3.flag_object(
    files, 'Shadowheart_AnotherSwimmingLesson', bg3.OBJECT_FLAG, flag_uuid='46190b70-0be5-4f11-834c-59b278211de2', description='Triggers the skinny dipping cutscene one more time')

# Shadowheart_Tav_State_Married flag
Shadowheart_Tav_State_Married = bg3.flag_object(
    files, 'Shadowheart_Tav_State_Married', bg3.GLOBAL_FLAG, flag_uuid='9d34a5e6-8e66-42d6-affa-85ff0c2780b4', description='Tav and Shadowheart are married')

# Shadowheart_State_DontHireDapperDrowPromise flag
Shadowheart_State_DontHireDapperDrowPromise = bg3.flag_object(
    files, 'Shadowheart_State_DontHireDapperDrowPromise', bg3.OBJECT_FLAG, flag_uuid='6b71d4ba-373d-4332-bd8b-84faeee3d768', description='This character promised their romantic partner to not hire drow twins')

# Shadowheart_State_RejectedDapperDrow flag
Shadowheart_State_RejectedDapperDrow = bg3.flag_object(
    files, 'Shadowheart_State_RejectedDapperDrow', bg3.OBJECT_FLAG, flag_uuid='0ff9ee19-b9ca-40e1-b67f-f5f172fb83f9', description='This character made their mind to not hire drow twins')

# Shadowheart_State_RejectedDapperDrow3some flag
Shadowheart_State_RejectedDapperDrow3some = bg3.flag_object(
    files, 'Shadowheart_State_RejectedDapperDrow3some', bg3.OBJECT_FLAG, flag_uuid='e9d590df-3c6e-48c5-b19e-7ad3899b4eab', description='This character and their partner made their minds to not hire drow twins')

# Shadowheart_Approval_Subtract_10 flag
Shadowheart_Approval_Subtract_10 = bg3.flag_object(
    files, 'Shadowheart_Approval_Subtract_10', bg3.OBJECT_FLAG, flag_uuid='f6bff638-5de1-4ac5-9e6f-c2c61206f952', description="Reduce Shadowheart's approval of Tav by 10")

# Shadowheart_Approval_Set_To_35 flag
Shadowheart_Approval_Set_To_35 = bg3.flag_object(
    files, 'Shadowheart_Approval_Set_To_35', bg3.OBJECT_FLAG, flag_uuid='a562c158-cb0c-40a9-9f34-44f76bfdfbf6', description="Reduce Shadowheart's approval of Tav to 35")

# Shadowheart_Approval_Set_To_Zero flag
Shadowheart_Approval_Set_To_Zero = bg3.flag_object(
    files, 'Shadowheart_Approval_Set_To_Zero', bg3.OBJECT_FLAG, flag_uuid='add81fd0-0641-45d3-8020-29098ccc22d7', description="Reduce Shadowheart's approval of Tav to naught")

# Shadowheart_Approval_Set_To_Neutral flag
Shadowheart_Approval_Set_To_Neutral = bg3.flag_object(
    files, 'Shadowheart_Approval_Set_To_Neutral', bg3.OBJECT_FLAG, flag_uuid='42a1da52-ccf5-46a0-954d-8f1c53dd20b6', description="Reduce Shadowheart's approval of Tav to the 'neutral' level")

# Shadowheart_Approval_Set_To_Low flag
Shadowheart_Approval_Set_To_Low = bg3.flag_object(
    files, 'Shadowheart_Approval_Set_To_Low', bg3.OBJECT_FLAG, flag_uuid='2701e07a-73a2-4b96-9951-9080555f3f8f', description="Reduce Shadowheart's approval of Tav to the 'low' level")

# Shadowheart_Approval_Set_To_VeryLow flag
Shadowheart_Approval_Set_To_VeryLow = bg3.flag_object(
    files, 'Shadowheart_Approval_Set_To_VeryLow', bg3.OBJECT_FLAG, flag_uuid='c80bad74-7669-4989-a912-106fd2ed4cd9', description="Reduce Shadowheart's approval of Tav to the 'very low' level")

# Shadowheart_BreakUp_Notification_Start flag
Shadowheart_BreakUp_Notification_Start = bg3.flag_object(
    files, 'Shadowheart_BreakUp_Notification_Start', bg3.OBJECT_FLAG, flag_uuid='d20cc281-6ed6-4e9b-bad5-28d403a2b0af', description='Tav did something stupid and Shadowheart broke up with them')

# Shadowheart_BreakUp_Notification_Finish flag
Shadowheart_BreakUp_Notification_Finish = bg3.flag_object(
    files, 'Shadowheart_BreakUp_Notification_Finish', bg3.OBJECT_FLAG, flag_uuid='80a1a14e-f831-4b3f-815a-684dc15f77e7', description='Shadowheart told Tav she has broken up with them')

# Tav_Regrets_Mizora_Romance flag
Tav_Regrets_Mizora_Romance = bg3.flag_object(
    files, 'Tav_Regrets_Mizora_Romance', bg3.OBJECT_FLAG, flag_uuid='54b85a7f-cc01-4391-8948-b637e9688aa5', description='Tav told Mizora they regret every moment they spent with her in the hells')

# Tav_Protected_Astarion flag
Tav_Protected_Astarion = bg3.flag_object(
    files, 'Tav_Protected_Astarion', bg3.GLOBAL_FLAG, flag_uuid='ea2d64c0-1043-487b-8656-4813b3c590df', description='Tav protected Astarion from Gandrel')

# Tav_Betrayed_Astarion flag
Tav_Betrayed_Astarion = bg3.flag_object(
    files, 'Tav_Betrayed_Astarion', bg3.GLOBAL_FLAG, flag_uuid='e688d213-2d07-4f29-af3a-24ff4f2ae6fa', description='Tav betrayed Astarion and surrendered him to Gandrel')

# Shadowheart_Reacted_Astarion_Protected flag
Shadowheart_Reacted_Astarion_Protected = bg3.flag_object(
    files, 'Shadowheart_Reacted_Astarion_Protected', bg3.GLOBAL_FLAG, flag_uuid='bd1887c7-a44f-4dbd-a7c3-19d0485350de', description='Shadowheart reacted to Tav protecting Astarion from Gandrel')

# Shadowheart_Reacted_Astarion_Betrayed flag
Shadowheart_Reacted_Astarion_Betrayed = bg3.flag_object(
    files, 'Shadowheart_Reacted_Astarion_Betrayed', bg3.GLOBAL_FLAG, flag_uuid='7bf95122-f0dd-4f07-bdb2-647edcbac6e9', description='Shadowheart reacted to Tav betraying Astarion from Gandrel')

# Tav_Shadowheart_Marriage_Mentioned flag
Tav_Shadowheart_Marriage_Mentioned = bg3.flag_object(
    files, 'Tav_Shadowheart_Marriage_Mentioned', bg3.LOCAL_FLAG, flag_uuid='dfed76e7-7716-47c4-abc3-3217493fec66', description="Shadowheart told Tav she's still getting used to being married")

# Tav_Shadowheart_Marriage_Mentioned flag
Tav_Shadowheart_Grandchildren_Mentioned = bg3.flag_object(
    files, 'Tav_Shadowheart_Grandchildren_Mentioned', bg3.LOCAL_FLAG, flag_uuid='89a8ddee-6dce-46a0-9ca4-7a67feca6735', description="Shadowheart told Tav she's expecting")

# Tav_Shadowheart_Epilogue_Convesation_Happened flag
Tav_Shadowheart_Epilogue_Convesation_Happened = bg3.flag_object(
    files, 'Tav_Shadowheart_Epilogue_Convesation_Happened', bg3.LOCAL_FLAG, flag_uuid='4bb8d67c-e81c-47fa-b911-5ec8f191650e', description="Tav spoke to Shadowheart at the Epilogue party")

# Betrayed_Shadowheart flag
Betrayed_Shadowheart = bg3.flag_object(
    files, 'Betrayed_Shadowheart', bg3.OBJECT_FLAG, flag_uuid='414f6e7d-4a86-4cdf-b5aa-31d053ae76d9', description="Tav betrayed Shadowheart.")

# Companion_Permanently_Leaves_Party flag
Companion_Permanently_Leaves_Party = bg3.flag_object(
    files, 'Companion_Permanently_Leaves_Party', bg3.OBJECT_FLAG, flag_uuid='76339e33-bb45-4f1b-9d43-58773590175c', description="Companion permanently leaves the party.")

# Companion_Attacks_Player flag
Companion_Attacks_Player = bg3.flag_object(
    files, 'Companion_Attacks_Player', bg3.OBJECT_FLAG, flag_uuid='b437177d-ac5d-4c44-a927-9a54b7f72bd2', description="Tav did something awful. Good-aligned companion attacks.")

# Companion_Attack_Target flag
Companion_Attack_Target = bg3.flag_object(
    files, 'Companion_Attack_Target', bg3.OBJECT_FLAG, flag_uuid='1b4b377c-10c2-45eb-a475-6b4944995fbf', description="Set on a player that is attacked by a companion")

# Post_Betrayal_InParty_Fight flag
Post_Betrayal_InParty_Fight = bg3.flag_object(
    files, 'Post_Betrayal_InParty_Fight', bg3.OBJECT_FLAG, flag_uuid='b482fd66-55ef-42e3-9922-347ed847c39d', description="A fight erupted in party because Shadowheart was betrayed.")

# Found_Memorable_Locations flag
Found_Memorable_Locations = bg3.flag_object(
    files, 'Found_Memorable_Locations', bg3.OBJECT_FLAG, flag_uuid='ac830dd2-bad2-44aa-9970-136c16477500', description="This character found 2 or more of Shadowheart's memorable locations in Baldur's Gate.")

# Tav_Mocked_Sharran_Prayer
Tav_Mocked_Sharran_Prayer = bg3.flag_object(
    files, 'Tav_Mocked_Sharran_Prayer', bg3.OBJECT_FLAG, flag_uuid='fa8d440f-1f40-4efe-b34c-a2a164e504de', description="Tav mocked her prayer. Bastard.")

# Tav_Prayed_With_Her
Tav_Prayed_With_Her = bg3.flag_object(
    files, 'Tav_Prayed_With_Her', bg3.OBJECT_FLAG, flag_uuid='e057c715-9a00-4bdd-b4dc-f60a20fa6d03', description="Tav prayed with Shadowheart to protect her from the shadows.")

# Tav_Already_Prayed_With_Her_Today
Tav_Already_Prayed_With_Her_Today = bg3.flag_object(
    files, 'Tav_Already_Prayed_With_Her_Today', bg3.OBJECT_FLAG, flag_uuid='a2a96abb-1b40-42fe-9f8b-6685eb173c63', description="This flag prevents too many prayers. Only one per long rest.")

# Tav_Prayer_Event
Tav_Prayer_Event = bg3.flag_object(
    files, 'Tav_Prayer_Event', bg3.OBJECT_FLAG, flag_uuid='5dd7a483-0578-40bc-b172-a7aaccf32f80', description="Event: Tav wants to pray with Shadowheart.")


# Shadowheart_Has_Doubts_About_Tav flag
# d6fef6ce-129e-4edf-8f00-00e0ecb08052
# bff7d8ea-6bfd-4ce7-a2c3-5e775004938d
# 01944863-f589-41a5-9cd7-84d2bebc17ae
Shadowheart_Has_Doubts_About_Tav = bg3.flag_object(
    files, 'Shadowheart_Has_Doubts_About_Tav', bg3.OBJECT_FLAG, flag_uuid='2774e4ec-e92d-41c1-a4b0-c6ddc84417da', description="Tav did something that made Shadowheart question if they are a good match.")

# Shadowheart_Rejects_Proposal
Shadowheart_Rejects_Proposal = bg3.flag_object(
    files, 'Shadowheart_Rejects_Proposal', bg3.OBJECT_FLAG, flag_uuid='c8f7b189-ea19-4a74-b581-305abdc9eb19', description="Shadowheart will reject marriage proposal.")

# Cheated_On_Shadowheart flag
Cheated_On_Shadowheart = bg3.flag_object(
    files, 'Cheated_On_Shadowheart', bg3.OBJECT_FLAG, flag_uuid='94181834-3277-492b-b223-11309c7bd90c', description="Tav cheated on Shadowheart with dapper drows.")

# Shadowheart_Reacted_To_Cheating flag
Shadowheart_Reacted_To_Cheating = bg3.flag_object(
    files, 'Shadowheart_Reacted_To_Cheating', bg3.OBJECT_FLAG, flag_uuid='3b5b8a8a-3b0e-485c-970d-f0467de463c9', description="Shadowheart noticed that Tav's behavior changed.")

# Shadowheart_Approval_AtLeast_80
# 1b41d3ae-4747-4595-8f0a-04443356ce19
Shadowheart_Approval_AtLeast_80 = bg3.flag_object(
    files, 'Shadowheart_Approval_AtLeast_80', bg3.OBJECT_FLAG, flag_uuid='f1391075-7de2-450e-aac3-c33ff6b3d1dd', description="Tav has approval 80 or higher with Shadowheart.")

# Shadowheart_Approval_Tracking_Works
# 63f7d5b1-9d2c-48a5-b733-725932c019f0
Shadowheart_Approval_Tracking_Works = bg3.flag_object(
    files, 'Shadowheart_Approval_Tracking_Works', bg3.OBJECT_FLAG, flag_uuid='5f660cf8-4824-4930-a3f7-cc384c40c786', description="Lua script that tracks Shadowheart approval does work.")

# Shadowheart_Hesitated_To_Ask
Shadowheart_Hesitated_To_Ask = bg3.flag_object(
    files, 'Shadowheart_Hesitated_To_Ask', bg3.OBJECT_FLAG, flag_uuid='d8d602d9-d2ab-4a8e-8ffb-c465fd52ce18', description="Shadowheart hesitated to ask about sleeping in one bedroll with Tav")

# Tav_Noticed_Shadowheart_Hesitated_To_Ask
Tav_Noticed_Shadowheart_Hesitated_To_Ask = bg3.flag_object(
    files, 'Tav_Noticed_Shadowheart_Hesitated_To_Ask', bg3.OBJECT_FLAG, flag_uuid='7b7c0c83-d397-42c5-b0bd-847b1f28cce1', description="Tav noticed that something's bothering Shadowheart")

# Shadowheart_Tav_Sleep_Together
Shadowheart_Tav_Sleep_Together = bg3.flag_object(
    files, 'Shadowheart_Tav_Sleep_Together', bg3.OBJECT_FLAG, flag_uuid='0187f803-6b3c-4249-b5a8-0e968306978b', description="Shadowheart sleeps with Tav at night")

# Shadowheart_Tav_Slept_Together
Shadowheart_Tav_Slept_Together = bg3.flag_object(
    files, 'Shadowheart_Tav_Slept_Together', bg3.OBJECT_FLAG, flag_uuid='09caaa22-7045-4764-970b-f5f90fb32386', description="Shadowheart slept with Tav at night")

#Alternative_Night_Sleep_Scene
Alternative_Night_Sleep_Scene = bg3.flag_object(
    files, 'Alternative_Night_Sleep_Scene', bg3.GLOBAL_FLAG, flag_uuid='eff18d52-34d0-4578-8891-eb8e6bfdbf32', description="Alternative night sleep scene")

# Tav_Love_Confession
Tav_Love_Confession = bg3.flag_object(
    files, 'Tav_Love_Confession', bg3.GLOBAL_FLAG, flag_uuid='a2f0421c-74dd-4b91-ba6f-bc6c55629518', description="Tav made a love confession to Shadowheart")

# Cuddles_Love_You
Cuddles_Love_You = bg3.flag_object(
    files, 'Cuddles_Love_You', bg3.GLOBAL_FLAG, flag_uuid='89be9f46-7a1a-436b-9a79-9b00f347b545', description="Tav said I love you to Shadowheart after night time cuddles")

# Tav_Said_Love_You
Tav_Said_Love_You = bg3.flag_object(
    files, 'Tav_Said_Love_You', bg3.GLOBAL_FLAG, flag_uuid='ea47a913-77a8-4a7e-bdfb-a13880f25107', description="Tav said I love you to Shadowheart")

# Flags that enable aliases to recurring topics
Enable_Recurring_Convos = bg3.flag_object(
    files, 'Enable_Recurring_Convos', bg3.OBJECT_FLAG, flag_uuid = '3527c09b-f87b-45b1-9409-b580200e3e43', description = 'Enables recurring conversation')
Alias_Tell_Me_About_Fear = bg3.flag_object(
    files, 'Alias_Tell_Me_About_Fear', bg3.OBJECT_FLAG, flag_uuid = 'a95d68ed-7dda-4f88-b87f-72ec392b1dd8', description = 'Enables recurring conversation')
Alias_Whats_The_Story_Odd_Artifact = bg3.flag_object(
    files, 'Alias_Whats_The_Story_Odd_Artifact', bg3.OBJECT_FLAG, flag_uuid = '101981a9-174c-45ae-9941-4b74357f17e1', description = 'Enables recurring conversation')
Alias_Know_Each_Other = bg3.flag_object(
    files, 'Alias_Know_Each_Other', bg3.OBJECT_FLAG, flag_uuid = '06ba6e44-0173-42a3-a95b-5fe5c0a268a3', description = 'Enables recurring conversation')
Alias_I_Want_To_Get_To_Know_You_More = bg3.flag_object(
    files, 'Alias_I_Want_To_Get_To_Know_You_More', bg3.OBJECT_FLAG, flag_uuid = 'a1aa7dfa-ef5d-4564-9998-b68ae2c6837c', description = 'Enables recurring conversation')
Alias_You_Worship_Shar_Selune = bg3.flag_object(
    files, 'Alias_You_Worship_Shar_Selune', bg3.OBJECT_FLAG, flag_uuid = '7b1213bb-e445-4400-b9f9-54fc2cfbd62a', description = 'Enables recurring conversation')
Alias_Why_Were_You_In_Pain = bg3.flag_object(
    files, 'Alias_Why_Were_You_In_Pain', bg3.OBJECT_FLAG, flag_uuid = '94292c24-e227-4fab-851e-a182cec60695', description = 'Enables recurring conversation')
Alias_Flareups_Iam_Concerned_Low_Trust = bg3.flag_object(
    files, 'Alias_Flareups_Iam_Concerned_Low_Trust', bg3.OBJECT_FLAG, flag_uuid = '2584896c-6fed-4e6e-848d-e0972c00b452', description = 'Enables recurring conversation')
Help_Me_Understand_Wound = bg3.flag_object(
    files, 'Help_Me_Understand_Wound', bg3.OBJECT_FLAG, flag_uuid = 'ce68aebc-b27c-4e61-ba5a-24a92fa2a726', description = 'Enables recurring conversation')
Must_Be_Way_To_Heal_It = bg3.flag_object(
    files, 'Must_Be_Way_To_Heal_It', bg3.OBJECT_FLAG, flag_uuid = '383c8876-40e1-43de-8f0d-8ec44a164264', description = 'Enables recurring conversation')
The_Curse_Isnt_Affecting_You = bg3.flag_object(
    files, 'The_Curse_Isnt_Affecting_You', bg3.OBJECT_FLAG, flag_uuid = '3b815d3b-08b8-4c46-8d70-24421304a292', description = 'Enables recurring conversation')
Tell_Me_More_About_Mother_Superior = bg3.flag_object(
    files, 'Tell_Me_More_About_Mother_Superior', bg3.OBJECT_FLAG, flag_uuid = '862e6b7c-1a0d-43eb-b56f-b23db6995a5e', description = 'Enables recurring conversation')
That_Grave_Did_It_Mean_Something = bg3.flag_object(
    files, 'That_Grave_Did_It_Mean_Something', bg3.OBJECT_FLAG, flag_uuid = '4a84f553-7049-47fb-a5a9-d2b29e3ad464', description = 'Enables recurring conversation')
That_Graffiti_We_Saw = bg3.flag_object(
    files, 'That_Graffiti_We_Saw', bg3.OBJECT_FLAG, flag_uuid = '62428da4-ca1d-4554-86a0-e435422ae686', description = 'Enables recurring conversation')
So_You_Had_Hideout = bg3.flag_object(
    files, 'That_Graffiti_We_Saw', bg3.OBJECT_FLAG, flag_uuid = 'a1743ba8-e94f-49f5-b32c-1ebdf16495eb', description = 'Enables recurring conversation')

Alias_Memories_Discussion_Selune_Parents_Saved = bg3.flag_object(
    files, 'Alias_Memories_Discussion_Selune_Parents_Saved', bg3.OBJECT_FLAG, flag_uuid = '6f44b5c4-6c26-4b15-94cc-c5563b354408', description = 'Enables recurring conversation')
Alias_Memories_Discussion_Selune_Parents_Killed = bg3.flag_object(
    files, 'Alias_Memories_Discussion_Selune_Parents_Killed', bg3.OBJECT_FLAG, flag_uuid = '8129a3c6-ef60-49dd-b8a7-ea913787622a', description = 'Enables recurring conversation')
Alias_Memories_Discussion_Shar_Parents_Saved = bg3.flag_object(
    files, 'Alias_Memories_Discussion_Shar_Parents_Saved', bg3.OBJECT_FLAG, flag_uuid = 'eaeb70fe-f296-452a-bae9-4983611e4724', description = 'Enables recurring conversation')
