# Origins and Companions: UUIDs
UUID_Shadowheart = '2bb39cf2-4649-4238-8d0c-44f62b5a3dfd'


# Origins and Companions: speaker uuids; these are global templates UUIDs and used in dialogs to refer to speakers
SPEAKER_MINSC       = '0de603c5-42e2-4811-9dad-f652de080eba'
SPEAKER_MINTHARA    = '25721313-0c15-4935-8176-9f134385451b'
SPEAKER_KARLACH     = '2c76687d-93a2-477b-8b18-8a14b549304c'
SPEAKER_SHADOWHEART = '3ed74f06-3c60-42dc-83f6-f034cb47c679'
SPEAKER_LAEZEL      = '58a69333-40bf-8358-1d17-fff240d7fb12'
SPEAKER_HALSIN      = '7628bc0e-52b8-42a7-856a-13a6fd413323'
SPEAKER_JAHEIRA     = '91b6b200-7d00-4d62-8dc9-99e8339dfa1a'
SPEAKER_GALE        = 'ad9af97d-75da-406a-ae13-7071c563f604'
SPEAKER_WYLL        = 'c774d764-4a17-48dc-b470-32ace9ce447d'
SPEAKER_ASTARION    = 'c7c13742-bacd-460a-8f65-f864fe41f255'
SPEAKER_DURGE       = 'e6b3c2c4-e88d-e9e6-ffa1-d49cdfadd411'
SPEAKER_BOO         = 'd49e3b49-a089-4465-b453-28dc79e82bb3'
SPEAKER_MIZORA      = '491a7686-3081-405b-983c-289ec8781e0a'
SPEAKER_VICONIA     = 'b1ea974d-96fb-47ca-b6d9-9c85fcb69313'
SPEAKER_ARNELL      = 'c12d561f-beae-4ef6-917e-0bec2f829449'
SPEAKER_NYM_ORLYTH  = '7574fc5a-3645-4370-a778-0b38d0ef162a'
SPEAKER_SORN_ORLYTH = 'f25b5f9a-bfde-4d81-a3fb-74fc39dad95b'
SPEAKER_GANDREL     = '0e47fcb9-c0c4-4b0c-902b-2d13d209e760'
SPEAKER_JERGAL      = '0133f2ad-e121-4590-b5f0-a79413919805'

# Origins and Companions: UUIDs, these are used in reactions
ORIGIN_SHADOWHEART = '2bb39cf2-4649-4238-8d0c-44f62b5a3dfd'
ORIGIN_ASTARION    = '3780c689-d903-41c2-bf64-1e6ec6a8e1e5'
ORIGIN_LAEZEL      = 'fb3bc4c3-49eb-4944-b714-d0cb357bb635'
ORIGIN_GALE        = '35c3caad-5543-4593-be75-e7deba30f062'
ORIGIN_WYLL        = 'efc9d114-0296-4a30-b701-365fc07d44fb'
ORIGIN_DARK_URGE   = '5af0f42c-9b32-4c3c-b108-46c44196081b'
ORIGIN_JAHEIRA     = 'c1f137c7-a17c-47b0-826a-12e44a8ec45c'
ORIGIN_MINTHARA    = 'eae09670-869d-4b70-b605-33af4ee80b34'
ORIGIN_MINSC       = 'e1b629bc-7340-4fe6-81a4-834a838ff5c5'
ORIGIN_HALSIN      = 'a36281c5-adcd-4d6e-8e5a-b5650b8f17eb'
ORIGIN_ALFIRA      = '38357c93-b437-4f03-88d0-a67bd4c0e3e9'
ORIGIN_KARLACH     = 'b8b4a974-b045-45f6-9516-b457b8773abd'

SPEAKER_TO_ORIGIN_MAP = {
    SPEAKER_SHADOWHEART : ORIGIN_SHADOWHEART,
    SPEAKER_ASTARION    : ORIGIN_ASTARION,
    SPEAKER_LAEZEL      : ORIGIN_LAEZEL,
    SPEAKER_GALE        : ORIGIN_GALE,
    SPEAKER_WYLL        : ORIGIN_WYLL,
    SPEAKER_DURGE       : ORIGIN_DARK_URGE,
    SPEAKER_JAHEIRA     : ORIGIN_JAHEIRA,
    SPEAKER_MINTHARA    : ORIGIN_MINTHARA,
    SPEAKER_MINSC       : ORIGIN_MINSC,
    SPEAKER_MINSC       : ORIGIN_HALSIN,
    SPEAKER_KARLACH     : ORIGIN_KARLACH
}

# Peanuts
PEANUT_SLOT_0 = 'PEANUT_SLOT_0'
PEANUT_SLOT_1 = 'PEANUT_SLOT_1'
PEANUT_SLOT_2 = 'PEANUT_SLOT_2'
PEANUTS = frozenset((PEANUT_SLOT_0, PEANUT_SLOT_1, PEANUT_SLOT_2))

# Current player speaker uuid
SPEAKER_PLAYER      = 'e0d1ff71-04a8-4340-ae64-9684d846eb83'

# Difficulty classes
Act1_Zero = '4dfcb0ff-e02a-4efd-b132-77dfd956055e'
Act1_Negligible = '2728289e-841d-4273-a29a-f24ae9f8c4fb'
Act1_VeryEasy = '8d398021-34e0-40b9-b7b2-0445f38a4c0b'
Act1_Easy = '31e92da6-bac9-46f7-af99-5f33d98fd4f0'
Act1_Medium = 'fa621d38-6f83-4e42-a55c-6aa651a75d46'
Act1_Challenging = '5e7ff0e9-6c80-459c-a636-3a3e8417a61a'
Act1_Hard = '831e1fbe-428d-4f4d-bd17-4206d6efea35'
Act1_VeryHard = '8986db4d-09af-46ee-9781-ac88ec10fa0e'
Act1_NearlyImpossible = 'ea049218-36a8-4440-a3fc-f3019a57c86b'
Act2_VeryEasy = '9d1f2171-fef1-4c03-9e83-523485174c46'
Act2_Easy = '0d9484eb-f680-4a33-853d-46fda64883f2'
Act2_Medium = '89f0acd4-346f-479d-8b7a-1a3eb5382f6d'
Act2_Challenging = 'c44bfd7d-84de-4568-9c57-a059b8df5435'
Act2_Hard = '91fb3598-dd68-4fa8-a306-2c7284709b08'
Act2_VeryHard = 'f3aa825b-785e-4f4a-90af-565c7e943609'
Act2_ExtraHard = '753ed8df-b5dc-4584-b9fa-de18c4c956b2'
Act2_NearlyImpossible = '52918812-bc1c-43b5-881a-58443902f5fa'
DC_Act3_VeryEasy = 'b9cea18d-f40a-444d-a692-76582a69130c'
DC_Act3_Easy = '5028066b-6ea0-4a6a-9e3e-53bee62559a7'
DC_Act3_Medium = '77cee1c4-384a-4217-b670-67db3c7add57'
DC_Act3_Challenging = '96bc76f2-0b2e-4a79-854f-e4971a772c36'
DC_Act3_Hard = '6298329e-255c-4826-9209-e911873b64e7'
DC_Act3_VeryHard = '60916b01-ba4c-418e-9f30-19a669704b4d'
DC_Act3_NearlyImpossible = '7bf230a0-b68a-4c79-a785-79b498d6c36b'

# Flags
FLAG_IMPOSSIBLE = '6e4b66e9-0f72-5171-04ba-441108b45b0e' # cut content
FLAG_ORI_Inclusion_Random = '5c169560-2732-c515-9e73-06ba1fd768f0' # Object flag. Set to true on Tav to pick a companion at random.
FLAG_ORI_Inclusion_PickedAtRandom = '46a601fb-8cb7-46ed-9856-3d4e38c53a02' # Object flag. Companion was picked at random after setting FLAG_ORI_Inclusion_Random.
FLAG_ORI_Shadowheart_Knows_WolfFear = 'f5f935c3-7f73-4de4-9aee-553cb96fb6d1' # Knows about Shadowheart's wolf fear
FLAG_ShadowHeart_InParty_Knows_SharWorshipper = '634f858d-9b54-0711-e31f-075d304422ab' # Global flag, Tav knows about Shar worship
FLAG_ORI_Shadowheart_Romance1_AfterCelebration_State_QueueInvitation = '2d7e1f5e-fee1-4732-a0a2-f1337cc5466c' # Invitation to the waterfall romance cutscene

# Shadowheart states
FLAG_ORI_Shadowheart_State_IrregularBehaviour = 'a1e4a324-4c58-48fb-b08e-d538fec45af8' # Global flag. Shadowheart is behaving oddly in camp.
FLAG_ORI_Shadowheart_State_EnemyOfSharPath = '055bbe0f-05f5-444b-a7e2-0f66edd2178c' # Global flag. Shadowheart rejected Shar
FLAG_ORI_Shadowheart_State_SharPath = 'bf9ae334-ff6a-458d-b898-3074bca0bdfb' # Global flag. Shadowheart remained loyal to Shar
FLAG_ORI_Shadowheart_State_HairChange = '2abcff91-1f1e-4853-98e2-ad7d2020158c' # Global flag. Change Shadowheart's hair to her new hairstyle.
FLAG_ORI_Shadowheart_State_SparedViconia = 'cd5421b3-6051-4641-a56f-69588173c13c' # Global flag. Shadowheart let Vicona live.
FLAG_ORI_Shadowheart_State_KilledViconia = '472e18f2-15f9-4004-bdae-a9340fff7b15' # Global flag. Shadowheart killed Viconia.
FLAG_ORI_State_ShadowheartIsDating = '3b35c15c-465a-433b-876d-0717287629b3' # Global flag. Shadowheart is dating someone.
FLAG_ORI_State_DatingShadowheart = 'e87f1e21-a758-47ae-8c0e-9e715eb289b5' # This character has started on the path to a relationship with Shadowheart.
FLAG_ORI_State_PartneredWithShadowheart = '3808ae35-ad4e-465b-800b-63d32b77211e' # This character is in an exclusive relationship with Shadowheart
FLAG_ORI_State_WasPartneredWithShadowheart = '542e6cf4-bfd1-471d-b4b5-693d630376cb' # Player was in a relationship with Shadowheart.
FLAG_ORI_Shadowheart_State_WasHugged = 'a9e3314f-8255-48dc-a764-37ea96d86924' # Global flag. Shadowheart was hugged by someone
FLAG_ORI_State_HandledBreakupWithShadowheart = 'd400a4f6-4a10-48a4-a425-73786e473815' # Shadowheart reacted to the player breaking up with her.
FLAG_ORI_Shadowheart_State_Act3RomanceEnded = '4f67ad76-c654-490e-ab62-263ae8fa8d14' # 
FLAG_ORI_Shadowheart_State_RejectShar_KilledParents = 'e9060caf-66b0-4701-8dfd-5ae1125f5afd' # Killed parents while on the reject shar path
FLAG_ORI_Shadowheart_State_RejectShar_SavedParents = '486d69d4-a7c2-4cb5-8fcb-8f2cb738ada9' # Saved parents while on the reject shar path
FLAG_ORI_Shadowheart_State_Shar_SavedParents = '8a0fad17-1615-4a0d-a045-21661d9a2aa0' # Saved parents while on shar path
FLAG_ORI_Shadowheart_State_Shar_KilledParents = '3a3b0ecf-a1ed-4733-8548-0348befc6bac' # Killed parents while on Shar Path
FLAG_ORI_Shadowheart_State_RetiredToFarmWithAvatar = '25930d25-598a-8692-5a96-039c9b2c0512' # Tav and Shadowheart retired to live in a farmhouse

FLAG_GEN_SoloPlayer = '29e32f83-2001-0dbc-7df9-3ca2b3bc4349'

# Astarion states
FLAG_ORI_Astarion_State_StayedVampireSpawn = '2724b881-6be1-49a7-8375-a49e9acb4546' # Astarion chose to stay a Vampire Spawn
FLAG_ORI_Astarion_State_BecameVampireLord = 'c446ce94-efd8-45d5-b407-284177b6b57e' # Astarion became a Vampire Lord

# Gale states
FLAG_ORI_Gale_Event_BombDisarmed = '3d014e79-5595-9365-87bb-5cbb1f87fe5c' # Gale's bomb was disarmed.

# Wyll states
FLAG_CAMP_MizorasPact_State_WyllReleasedFromPact = '79a90490-b009-507c-e0d3-f79b0bdd4cb6' # Wyll was released from his pact, Ravengard is doomed to the hells
FLAG_GLO_Wyll_State_GrandDuke = '0e223e4d-be63-89f4-380f-5cc755817abd' # Wyll chose to become Grand Duke before endgame
FLAG_CAMP_MizorasPact_State_WyllEternalPact = '8da8b1fb-5aa9-8cf5-8b45-6f8ca31a1227' # Wyll is eternally pacted to Mizora
FLAG_GLO_Wyll_State_BladeOfFrontiers = '8c46322f-7965-94c7-1318-62c391f1c8f1' # Wyll endgame state: he has chosen to remain the Blade of Frontiers
FLAG_GLO_Wyll_State_BladeOfAvernus = 'faeb73da-a609-dc56-7745-ac07f795c137' # Wyll's end game state: Blade of Avernus

# Minthara states
FLAG_ORI_Minthara_State_AskedAboutAllCurrentTeamMembers = '6efc8f72-ace6-8414-bb77-862f9dd4d6a5' # Object flag. Asked Minthara about all current Team Members

FLAG_OriginRemoveFromPartyAfterDialog = '7a429beb-fbfb-fa8a-3a33-0349323ad11d' # Set on a companion. They return to camp after the dialog.

FLAG_ORI_Shadowheart_Event_PostNightfall_DiscussionAvailable = '1eefa664-d8c5-6f9e-e662-66625481a89b' # Global flag. Sets when the follow-up to SH nightfall SD ROM is available
FLAG_ORI_Shadowheart_State_PostSkinnyDipping_DiscussionAvailable = '741d48eb-112e-6419-3a67-7b8e5928d7e1' # Global flag. Sets when follow-up discussion to the skinnydipping SD ROM is available
FLAG_Shadowheart_InParty_Event_SkinnyDipStart = '0b659872-c728-4d0d-934d-34c3609cdeb7'
FLAG_ORI_State_PartneredCompanionIncluded = 'c401d64f-025e-433d-911d-1e32d0da37fa' # Player's partnered companion has been included to the current dialog (gets cleared when speaker leaves the dialog).
FLAG_CAMP_Halsin_CRD_Romance_PartnerAllowsHalsin = '2c588e1e-8acb-4c89-8c82-3db5979eb117' # Sets if your existing partner is ok with sharing you with Halsin
FLAG_CAMP_Halsin_CRD_Romance_PartnerDoesNotAllowHalsin = '3dba761a-28cc-4d6d-9af2-1e3835cf9321' # Sets when your existing partner is not ok with sharing you with Halsin
FLAG_GLO_Halsin_Knows_ShadowCurse = '4bfcb6bc-07e0-0cc5-637d-c59f137caa78' # Halsin told the party about the shadow curse
FLAG_Shadowheart_InParty_Event_HappenedThought = '8a9eecb6-3a5c-4292-b0d5-9a3b23d7c5e3' # Tav asked "What do you think of all that's happened to us so far?"
FLAG_LOW_SharGrotto_ConfrontViconia_SharranAlliance = 'ea829b7c-5f69-c4fc-6b4c-b8a190d31a86' # Sets when the player is offered the support of the Shar Grotto
FLAG_ORI_Shadowheart_ShadowheartBetrayed = 'f78e829a-55cb-4dbf-859e-2f125471fbdc' # Sold Shadowheart to Viconia
FLAG_LOW_SharGrotto_Event_SurrenderShadowheart = 'bfc7f3b7-4e58-44e1-bb58-131ee77fc0ad' # Give Shadowheart to Viconia
FLAG_ORI_State_Recruited = 'e78c0aab-fb48-98e9-3ed9-773a0c39988d' # Set on recruited companions
FLAG_GLO_Minthara_InParty_HasTopicalGreeting = '8069e1a8-51b5-afc0-de8c-f5af844f034d' # Object flag. Minthara has a topical greeting in place of normal greeting

FLAG_VISITEDREGION_SCL_Main_A_ACT_2 = 'f6e72539-9bc6-42e1-a20f-390f3a17ad8d' # Global flag. Player visited shadow cursed lands.
FLAG_VISITEDREGION_INT_Main_A_ACT_3 = 'a2e1a618-d211-484e-9389-6b37308b8da1' # Global flag. The party had camped in a region between acts 2 and 3.
FLAG_COL_PartyProgress_EnteredColony = '666abe92-f197-4c38-85a8-d879a9e258b6' # Global flag. Players entered the Colony

FLAG_LOW_BhaalTemple_State_KilledVictim = 'ba91f332-45d5-483c-b460-dfec2e6d87e9' # Global flag. Flag set in dialog when Orin stabs the victim.

DEN_PartyProgress_EnteredGrove = '18cfaaeb-c0df-46ac-962d-0c300f816d73' # Global flag. At least one player entered the grove
GOB_State_LeadersAreDead = 'a1c5b01f-4b7f-47ab-82b0-d24d9c6d8bc6' # Global flag. Goblin leaders are dead
DEN_GoblinHunt_Event_LeaderMetPlayer = '097d69b7-7e59-49ba-830a-b2b7f950aec7' # Global flag. Flag set once the designated leader of the tieflings has met a player at the entrance of the Grove.
DEN_AttackOnDen_State_DenVictory = '71c7f23e-3ff1-c9b8-3ef5-d75fa1b42c8d' # Global flag. The tieflings won Attack on Den or Goblin Hunt was completed
DEN_AttackOnDen_State_RaiderVictory = 'abe1bce8-c234-4afe-a490-76210d98a078' # Global flag. Tieflings in the den were killed during Attack On Den
DEN_Lockdown_State_Active = '0b54c7d2-b7b1-4d0f-b8e4-0cf1ee32b1eb' # Global flag. The Druids' Grove is under lockdown.

FLAG_ORI_Shadowheart_SeenWithBox = '31d00a1b-9f7b-7385-4d94-e6f98883742c' # Global flag. Tav has seen Shadowheart with the artifact.
FLAG_GOB_Orpheus_State_HadVoiceOfAbsoluteEvent = '9546407d-19e3-4f26-88af-5970896997d7' # Global flag. The player took part in Voice of Absolute dialog and saw Orpheus box protecting from the Voice.
FLAG_Act2_PointOfNoReturnReached = 'a3155f30-b8f3-4db5-ac21-d3036f4426e3' # Global flag. We entered the Shadowfell and the act 2 point of no return has been reached.


FLAG_Companion_Leaves_Party = "363c71f4-8b46-c0c0-4bbb-0e5a85e4652d" # If set on a companion, they leave the party

# Global flags that indicate whether an origin character is an avatar (a human controlled player) or a companion
FLAG_GLO_Origin_Avatar_Shadowheart = '1a2858f5-f481-4af8-9440-1a2315df86b8' # Set when Shadowheart is part of the team and avatar, regardless of whether in camp or in party
FLAG_GLO_Origin_PartOfTheTeam_Shadowheart = '7f9ac9e8-1e8d-4bf8-8716-68215f0f066e' # Set when Shadowheart is part of the team, meaning recruited, regardless of whether in camp or in party
FLAG_GLO_Origin_Avatar_Laezel = 'ecbab7a6-0a96-4c30-81d1-f70cc960b749' # Set when Laezel is part of the team and avatar, regardless of whether in camp or in party
FLAG_GLO_Origin_PartOfTheTeam_Laezel = '57d93a1d-4400-4307-845f-25d9a250d332' # Set when Laezel is part of the team, meaning recruited, regardless of whether in camp or in party
FLAG_GLO_Origin_Avatar_Astarion = '5304da6f-4174-4253-b456-de4b0aadb33c' # Set when Astarion is part of the team and avatar, regardless of whether in camp or in party
FLAG_GLO_Origin_PartOfTheTeam_Astarion = '24ae9cee-0516-47c6-8291-cb143256264d' # Set when Astarion is part of the team, meaning recruited, regardless of whether in camp or in party
FLAG_GLO_Origin_Avatar_Gale = '7e4814d1-d7f5-4fbd-a101-8492eea43072' # Set when Gale is part of the team and avatar, regardless of whether in camp or in party
FLAG_GLO_Origin_PartOfTheTeam_Gale = '4f1acb3b-17e8-4036-a43c-fc6ee2828061' # Set when Gale is part of the team, meaning recruited, regardless of whether in camp or in party
FLAG_GLO_Origin_Avatar_Wyll = '4a2d36e6-e036-48dd-9c89-b99a19c053a0' # Set when Wyll is part of the team and avatar, regardless of whether in camp or in party
FLAG_GLO_Origin_PartOfTheTeam_Wyll = '24e24ca7-3446-440b-b645-19404845e108' # Set when Wyll is part of the team, meaning recruited, regardless of whether in camp or in party
FLAG_GLO_Origin_Avatar_Karlach = 'b5ad4b07-9522-47ec-98e6-85c28df64dc5' # Set when Karlach is part of the team and avatar, regardless of whether in camp or in party
FLAG_GLO_Origin_PartOfTheTeam_Karlach = 'b1e6f12a-600a-4e2e-9871-b08a9fe3a617' # Set when Karlach is part of the team, meaning recruited, regardless of whether in camp or in party
FLAG_GLO_Jaheira_State_PermaDefeated = '932fb5a1-00ba-4621-b7ae-877d40d7ddcd' # Jaheira is permanently defeated
FLAG_GLO_Origin_PartOfTheTeam_Jaheira = 'd7d29efe-70bb-47c2-9db3-bc8a10347bc6' # Set when Jaheira is part of the team, meaning recruited, regardless of whether in camp or in party
FLAG_GLO_Origin_PartOfTheTeam_Minsc = '3510cd49-7ff6-475c-829b-d4d68a07b085' # Set when Minsc is part of the team, meaning recruited, regardless of whether in camp or in party


# Flags (kisses)
FLAG_ORI_Kiss_StartRandom = '2a98bc41-f6b7-4277-a282-1a91c4ef8a9b' # Set on speaker to start a random kiss selection.
FLAG_ORI_Kiss_EndRandom = 'f13348d0-34bf-4328-80a5-29dd8a7b0aef' # Clears random kiss selection
FLAG_ORI_Kiss_VersionA = '6061dd44-55fe-41b0-a79c-fc696073de0a'
FLAG_ORI_Kiss_VersionB = '8da83898-1476-43e7-ab38-314c61b1ff74'
FLAG_ORI_Kiss_VersionC = '98e473ed-0144-482c-853a-e4fc739646f5'
FLAG_ORI_Kiss_VersionD = '0bdf3afd-1997-4c9e-82f3-b1365a47034c'

# Shadowheart's romance scene
# "NIGHT_Shadowheart_Skinnydipping_9f583304-0a1a-498c-acf9-3c8dcc30ee3d"
FLAG_NIGHT_Shadowheart_Skinnydipping = '9f583304-0a1a-498c-acf9-3c8dcc30ee3d' # Romance night for skinny dipping with Shadowheart
FLAG_ORI_Shadowheart_Event_SkinnyDippingRomanceScene = '3437a073-b92a-4999-b6b9-e7745865a0c2' # Starts the skinny dipping romance scene
FLAG_ORI_Shadowheart_State_PostSkinnydipping_Discussed = 'f0a86777-beff-43ed-92e4-ebc1568c51fc' # Global flag. Sets once the follow-up to the Skinnydipping SD ROM has occurred.

# Camp state flags
FLAG_GLO_CAMP_State_NightMode = 'fb53edc2-9a89-4ad2-af83-20b5fe425cdd'
FLAG_CAMP_GLO_State_InCamp = '161b7223-039d-4ebe-986f-1dcd9a66733f' # Set on a character when they are in camp

FLAG_GLO_SafeRomance_Enabled = 'f46a2601-92d1-4b86-98b5-0dae4a290ff6' # Is the safe romance option enabled?

# Tags: 'really' tags
TAG_REALLY_SHADOWHEART = '642d2aee-e3df-47e3-9f47-bbcd441bb9e0'
TAG_REALLY_DARK_URGE = 'cd611d7d-b67d-42b4-a75c-a0c6091ef8a2'
TAG_REALLY_ASTARION = 'ffd08582-7396-4cac-bcd4-8f9cd0fd8ef3'
TAG_REALLY_GALE = '9b0354c0-56d9-4723-8034-918ac9abab19'
TAG_REALLY_HALSIN = '9b8709f9-8d2a-4b4e-a465-8505c561d7f5'
TAG_REALLY_JAHEIRA = '8457eb5f-036c-4143-b6cf-447a9f555c7a'
TAG_REALLY_KARLACH = '1a2f70d6-8ead-4eb5-a824-79ee1971764a'
TAG_REALLY_LAEZEL = 'b5682d1d-c395-489c-9675-1f9b0c328ea5'
TAG_REALLY_MINSC = 'aeb694fc-83fb-452d-819a-b97ba442dc42'
TAG_REALLY_MINTHARA = '3e84e1cd-2193-4f9f-80b4-c2ededefaea6'
TAG_REALLY_WYLL = '5f40def5-d3ec-4698-a367-01a339888956'

# Tags: other
TAG_SHADOWHEART = '8b4cf0fa-f712-4839-9439-f86a519078fa'
TAG_SHADOWHEART_ENEMYOFSHARPATH = '8eca8027-996c-4c61-bec6-77f853de295b'
TAG_SHADOWHEART_SHARPATH = '9624a3fe-bb9e-47c5-b9ab-417e6da6f84b'
TAG_SHORT = '50e7beca-4e90-43cd-b7c5-c235e236077f'
TAG_DWARF = '486a2562-31ae-437b-bf63-30393e18cbdd'
TAG_DRAGONBORN = '02e5e9ed-b6b2-4524-99cd-cb2bc84c754a'
TAG_GITH = '677ffa76-2562-4217-873e-2253d4720ba4'
TAG_GOBLIN = '608597d9-bf00-4ede-aabe-767457280925'
TAG_BODYTYPE_STRONG = 'd3116e58-c55a-4853-a700-bee996207397'
TAG_MALE = '8f74d144-041e-4035-a9ac-72f41fc32de7'
TAG_FEMALE = '3806477c-65a7-4100-9f92-be4c12c4fa4f'
TAG_FULL_CEREMORPH = '3797bfc4-8004-4a19-9578-61ce0714cc0b' # Player has become a full Mind Flayer
TAG_HUMANOID_MONSTER = '7fbed0d4-cabc-4a9d-804e-12ca6088a0a8'
TAG_AVATAR = '306b9b05-1057-4770-aa17-01af21acd650'

# Gods
GOD_Selune = '4533d292-5b1f-43c7-ad44-6bc7db1000ca'
GOD_Shar = '486e4a27-e6f9-40a5-9dd1-108a1d0f60eb'


# Approval flags
FLAG_Approval_AtLeast_60_For_Sp1  = '4445984d-56f3-0e7c-25d5-cf5cca2a5642'

FLAG_Approval_AtLeast_Neg20_For_Sp2 = '4c39c64b-8373-6f5f-2dac-990196d3c6dc'
FLAG_Approval_AtLeast_10_For_Sp2  = 'fccac36f-92a5-ad84-9e45-fed71d386452'
FLAG_Approval_AtLeast_30_For_Sp2  = '98ca7185-0f2d-4420-be81-2b7c5e109e91'
FLAG_Approval_AtLeast_40_For_Sp2  = 'cb50595f-b514-26a8-0c90-fbb21185b22e'
FLAG_Approval_AtLeast_60_For_Sp2  = 'bf670cb3-8110-e901-ed45-bb0b0f15b761'
FLAG_Approval_AtLeast_80_For_Sp2  = '4975d4b7-031d-7a78-778a-86b46503a224'

FLAG_Approval_AtLeast_10_For_Sp3  = 'be8510e8-0339-3fee-f198-b1dbe1a0b010'
FLAG_Approval_AtLeast_20_For_Sp3  = '1e3e9473-4277-79b5-42a2-cfd066386593'
FLAG_Approval_AtLeast_30_For_Sp3  = '534d898c-b83a-2523-eff2-e44fec0c207e'
FLAG_Approval_AtLeast_40_For_Sp3  = 'f1ab5792-7ebe-3021-bb12-e8b749507477'
FLAG_Approval_AtLeast_50_For_Sp3  = '1ab5dca5-dc29-9dcc-2f8f-bcc15147a15c'
FLAG_Approval_AtLeast_60_For_Sp3  = '379b2a1e-207f-fca8-b2e7-372dc8751a5d'
FLAG_Approval_AtLeast_70_For_Sp3  = '207d5eaa-871d-a8ff-7ef4-a3778ef41660'
FLAG_Approval_AtLeast_80_For_Sp3  = '5d4a8ffd-8e6b-f5ad-22f4-c4c21fe9f3e0'
FLAG_Approval_AtLeast_90_For_Sp3  = '4caef451-20b0-49ff-c5ad-954fadd29d44'
FLAG_Approval_AtLeast_100_For_Sp3 = '4c9f41f5-b15c-7c2b-b62e-9c9b16ca46f5'

FLAG_Approval_AtLeast_10_For_Sp7  = 'ad3eebe2-0608-3b7d-940d-0a5f89817009'
FLAG_Approval_AtLeast_20_For_Sp7  = 'dfc5c129-03de-43ec-1355-b91dd281d1d3'
FLAG_Approval_AtLeast_30_For_Sp7  = 'da1fcdc2-de0d-7ff8-0487-9b970cdb6a01'
FLAG_Approval_AtLeast_40_For_Sp7  = 'e4647aa3-27b6-9141-1852-c3cb9ad387dc'
FLAG_Approval_AtLeast_50_For_Sp7  = '558ee7d5-41ec-430e-2f6e-b88d0164dbc8'
FLAG_Approval_AtLeast_60_For_Sp7  = 'f5e9b2a3-7008-f239-ed0d-c8c93468f4a3'
FLAG_Approval_AtLeast_70_For_Sp7  = '5b917a54-1f88-8d60-bee2-a0cac84fa475'
FLAG_Approval_AtLeast_80_For_Sp7  = 'b62c330f-45c1-31f8-259c-1612e5bde942'
FLAG_Approval_AtLeast_90_For_Sp7  = 'b0467b67-bbe5-5835-2788-3060dae6e779'
FLAG_Approval_AtLeast_100_For_Sp7 = 'ebeb67a2-c031-0b10-9205-041ece18f242'

