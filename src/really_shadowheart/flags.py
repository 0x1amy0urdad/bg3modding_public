from __future__ import annotations

import bg3moddinglib as bg3

from .context import files


#################
# Custom flags
#################

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

# Under construction flag
Under_Construction = bg3.flag_object(
    files, 'Under_Construction', bg3.OBJECT_FLAG, flag_uuid='63ffe70f-4ad7-498c-966e-a47106e3b23d', description='Set to true to show unfinished content')

# Shadowheart needs a night to get her thoughts together
ORI_Shadowheart_AfterParents = bg3.flag_object(
    files, 'ORI_Shadowheart_AfterParents', bg3.OBJECT_FLAG, flag_uuid='6f8e2b2b-5ffa-4e83-adf7-d80a8e36a8d8', description='Shadowheart needs a night to get her thoughts together')

# Shadowheart cried and got her thoughts together
ORI_Shadowheart_CriedAfterParents = bg3.flag_object(
    files, 'ORI_Shadowheart_CriedAfterParents', bg3.OBJECT_FLAG, flag_uuid='4777f4c8-d5ee-4d4e-83cc-243b3c837fa8', description='Shadowheart cried and got her thoughts together')

# Loot_Viconias_Stuff flag
Loot_Viconias_Stuff = bg3.flag_object(
    files, 'Loot_Viconias_Stuff', bg3.OBJECT_FLAG, flag_uuid='550ff254-7218-4e11-9699-17d837da43f8', description="Loot Viconia's stuff")

# ORI_Shadowheart_State_SmilesWhenHugged
ORI_Shadowheart_State_SmilesWhenHugged = bg3.flag_object(
    files, 'ORI_Shadowheart_State_SmilesWhenHugged', bg3.OBJECT_FLAG, flag_uuid='3486a7e3-97c8-464b-9afa-665e8ec981ff', description='Shadowheart is hugged and she smiles')

# ORI_Shadowheart_State_HugsEnabled flag
ORI_Shadowheart_State_HugsEnabled = bg3.flag_object(
    files, 'ORI_Shadowheart_State_HugsEnabled', bg3.OBJECT_FLAG, flag_uuid='9402335a-e23e-464b-9c18-fb5fed9eff04', description='Shadowheart was hugged, she liked that and wants more hugs')

# ORI_Shadowheart_State_HugReaction
ORI_Shadowheart_State_HugReaction = bg3.flag_object(
    files, 'ORI_Shadowheart_State_HugReaction', bg3.OBJECT_FLAG, flag_uuid='b55cf115-9659-4b46-9150-ae4a261ea0af', description='Shadowheart reacts to the first hug when she is not sad')

# ORI_ShadowheartMoreOpportunitiesToSlipAway flag
ORI_ShadowheartMoreOpportunitiesToSlipAway = bg3.flag_object(
    files, 'ORI_ShadowheartMoreOpportunitiesToSlipAway', bg3.OBJECT_FLAG, flag_uuid='2f2779cf-4a7b-44ef-8458-d29b48578740', description='Shadowheart says that she hopes for more opportunities to slip away')

# ORI_LongRestBeforeMoreOpportunitiesToSlipAway flag
ORI_LongRestBeforeMoreOpportunitiesToSlipAway = bg3.flag_object(
    files, 'ORI_LongRestBeforeMoreOpportunitiesToSlipAway', bg3.OBJECT_FLAG, flag_uuid='fec1c849-c9b6-47ab-9dd4-84acff4cd01a', description='Wait 1 long rest before asking Shadowheart to slip away again')

# ORI_ShadowheartAnotherSwimmingLessonReplied flag
ORI_ShadowheartAnotherSwimmingLessonReplied = bg3.flag_object(
    files, 'ORI_ShadowheartAnotherSwimmingLessonReplied', bg3.OBJECT_FLAG, flag_uuid='8942cfa4-550f-482b-8b27-56625dee1c15', description='Shadowheart replied to a proposal of seizing an opportunity')

# ORI_ShadowheartAnotherSwimmingLesson flag
ORI_ShadowheartAnotherSwimmingLesson = bg3.flag_object(
    files, 'ORI_ShadowheartAnotherSwimmingLesson', bg3.OBJECT_FLAG, flag_uuid='46190b70-0be5-4f11-834c-59b278211de2', description='Triggers the skinny dipping cutscene one more time')

# ORI_Shadowheart_Tav_State_Married flag
ORI_Shadowheart_Tav_State_Married = bg3.flag_object(
    files, 'ORI_Shadowheart_Tav_State_Married', bg3.GLOBAL_FLAG, flag_uuid='9d34a5e6-8e66-42d6-affa-85ff0c2780b4', description='Tav and Shadowheart are married')

# ORI_State_DontHireDapperDrowPromise flag
ORI_State_DontHireDapperDrowPromise = bg3.flag_object(
    files, 'ORI_State_DontHireDapperDrowPromise', bg3.OBJECT_FLAG, flag_uuid='6b71d4ba-373d-4332-bd8b-84faeee3d768', description='This character promised their romantic partner to not hire drow twins')

# ORI_State_RejectedDapperDrow flag
ORI_State_RejectedDapperDrow = bg3.flag_object(
    files, 'ORI_State_RejectedDapperDrow', bg3.OBJECT_FLAG, flag_uuid='0ff9ee19-b9ca-40e1-b67f-f5f172fb83f9', description='This character made their mind to not hire drow twins')

# ORI_State_RejectedDapperDrow3some flag
ORI_State_RejectedDapperDrow3some = bg3.flag_object(
    files, 'ORI_State_RejectedDapperDrow3some', bg3.OBJECT_FLAG, flag_uuid='e9d590df-3c6e-48c5-b19e-7ad3899b4eab', description='This character and their partners made their minds to not hire drow twins')

# Shadowheart_Approval_Subtract_10 flag
Shadowheart_Approval_Subtract_10 = bg3.flag_object(
    files, 'Shadowheart_Approval_Subtract_10', bg3.OBJECT_FLAG, flag_uuid='f6bff638-5de1-4ac5-9e6f-c2c61206f952', description="Reduce Shadowheart's approval of Tav by 10")

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

# Shared_Future_With_Shadowheart flag
Shared_Future_With_Shadowheart = bg3.flag_object(
    files, 'Shared_Future_With_Shadowheart', bg3.OBJECT_FLAG, flag_uuid='d6fef6ce-129e-4edf-8f00-00e0ecb08052', description="This character agreed to share their future with Shadowheart.")

