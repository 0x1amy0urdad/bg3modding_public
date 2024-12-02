from __future__ import annotations

import bg3moddinglib as bg3

from .build import add_build_procedure
from .context import files

########################################################
# Create custom strings, put them in english.loca.xml
########################################################

def create_text_content() -> None:
    content = {
        "h744690e1g4055g49b9gba6cgf175c791781f": (1, ""),
        "hd32730e7ga6b4g43dag9392g6adbc215dc95": (1, "Rehearsal 1"),
        "h4fca3521g89b7g40c0g90a0gf0ca7f0bb638": (1, "Rehearsal 2"),
        "h53555b45g415ag423ag80a2g487622d41360": (1, "Rehearsal 3"),
        "h198df115g788ag4de4g9ccfg5c8e82bc10f8": (1, "Let's keep that our special secret. Oh you know what I mean..."),
        "he7d56031g63c2g4a69gacdcg1151b2bfc3b1": (1, "Shadowheart is in love with you"),
        "hcce3a355g2e43g4231g94fdg0d16de9a5cb8": (1, "No... it can't be true..."),
        "h79ae6514g939dg49eega50eg86bbf7381a35": (1, "I... it's difficult for me to talk about..."),
        "hd0509e5dgee24g4e38g9e53gd72e5795cba6": (1, "Checking in on me? I'm right where I'm supposed to be - with the man I love."),
        "hfee6d489g9f92g4b08gad5egcde430d9f6e3": (1, "&lt;i&gt;Wipe a happy tear and kiss her.&lt;/i&gt;"),
        "heb4bc4d7g7624g48b7g8200g7c599b41938f": (1, "We should take your parents with us to the next party, if Withers calls us again."),
        "h6af6d9f8gede1g482fg8cc6g0cecb08e0cfa": (1, "Wait, are you... Do you really mean that?"),
        "haadd3e89g0eeeg4514g9cf2g3a73b36b9f98": (1, "Did you just say that we are going to have a baby?!"),
        "hab27fa75ge385g4d81g8b81gca48789e9a7b": (1, "I do hope your parents would step in and help us with our new troubles..."),
        "hcb948f33g2863g49d1g8074g267265978b66": (1, "&lt;i&gt;Pay no attention to that and move on to other matters.&lt;/i&gt;"),
        "h8b4751f2g4391g412dg8f63gc05bf8c67056": (1, "What do you make of our encounter with the Gur monster hunter?"),
        "hb3033ad0gf4d6g41d7gba68gab137658a56a": (1, "Speaking truthfully, I'm a little surprised you chose to shield Astarion."),
        "hfc1897b2g015ag4589gbe29gff4cf74aff01": (1, "He's one of us. I wasn't about to just betray him."),
        "hbe191947g233fg4ef7gb172g415bdd40ba49": (1, "I just hope I don't come to regret standing by him."),
        "hc1913f71g45e1g4388g9a08gbbef9784d018": (1, "He knows too much - safer to keep him with us than risk him exposing our condition."),
        "h56359b73gb29ag4f19gbcd0gcd15a66d30f6": (1, "How adorable. Such camaraderie at such a bargain rate."),
        "h18a8a0c7g2147g42beg8a5fgdedc6b33b731": (1, "You're as loyal as a pup and twice as handsome."),
        "haab6ee84g0a04g403dga445g5d9e7088377b": (1, "You're as loyal as a pup and twice as pretty."),
        "h3ce42409g98f5g4c9bgaf28ge161d5015c0a": (1, "You're as loyal as a pup and twice as charming."),
        "h2351244eg25b9g4136ga0e4gec799138c580": (1, "Well you can always rid yourself of that regret with a well-place thrust of a dagger... if it comes to that, of course."),
        "hf78f63ffg0e44g4359ga02cg205cb18ab600": (1, "Very strategic of you, actually. Hopefully keeping him in our midst proves to be the lesser risk."),
        "hed5250f0g98dag42efga79ag3b0d5fb8f44c": (1, "I deserve to be hated for what I did. All I can say, don't leave me... although I cannot give you a reason not to."),
        "hbf3e9b58gce14g484bga545g9cfb5645c4cb": (1, "If we agree on that, we can turn the page now, shall we?"),
        "h757179ffg608bg47e6gaf76gb55db99ca2c8": (1, "Are you being sarcastic now?"),
        "h9188942ag8b41g4e68g894ag277ae309838f": (1, "We need allies for the fight to come. I tried to win Mizora's favor. I have no feelings for her."),
        "hfb28a99dg8cc8g4ad3g879bg6f843e2112d8": (1, "I do mean it. I regret every moment I spent in the Hells with Mizora."),
        "hfc18b96ege9ccg484ag946fg3aa2a789e477": (1, "You don't believe me, do you?"),
        "h52c04688gf4a9g4178ga99eg7f58bfe6fae5": (1, "I admit it, I was a fool and I regret what I've done. You must be hating me, and I absolutely deserve that."),
        "h1f7912b4g8b72g46ceg9e8bg8c9874f03472": (1, "Don't be foolish - you're far too handsome to hate. I'll still pet you as much as you like."),
        "h63ebfa3egc78eg487cga031g3cbc4b395e4a": (1, "You saw me with Mizora that evening, did you? Why didn't you talk me out of it?"),
        "hee80ea70g5160g490agac63g98f23b7d0501": (1, "Listen, Shadowheart. She's a half devil, she charmed, she tempted me. It meant nothing, I swear."),
        "h06a5cd66g501bg402bgb1e3g41bd32d9ca18": (1, "Others seem quite tired, they'll be asleep soon. Don't you think we could seize the opportunity?"),
        "h0a14be70g6828g4ed5g8202g288788d68b6e": (1, "What more could I need? If I had all that, and I had you... Yes. I want to share everything that lies ahead of me with you."),
        "h0d2027f1g386eg45bbg8a6ag7ab77f651a6c": (1, "A lot's changed since then. More than I ever thought was possible."),
        "h11a84dedgd2cbg46bfg8b92ga6c48d37a486": (1, "I really fell for you, you know. But then... You've changed, and not for the better. I can't be at such odds with you and be your lover. Not anymore."),
        "h2155d8e8g3584g48fbg95fdg5651ebed00ee": (1, "I want to spend my life with you. Would you marry me?"),
        "h22d5d4fegda81g4379g9e0cge6ff376a3252": (1, "I want to be by your side."),
        "h40c1c09egd7bcg4575g8a9dgd8ee7a05e75d": (1, "Wait until the others are asleep, then come with me... Get some rest while you can."),
        "h4e692070gf12fg40e1g9b36ge64802670e20": (1, "Wait, I don't want to lose you... I want to be with you..."),
        "h55a00408g3549g4916g96d9g0837ef055041": (1, "Only if you kiss me."),
        "h5de64a8eg404fg4151ga564g5956eab0a0f4": (1, "Perhaps, you're right. It would be best for us if we end what we had."),
        "h5def25a4gf970g4dadgbb68gec13e203facc": (1, "I'm just trying to get you jealous, my love. Of course I wasn't going to hire their services."),
        "h694c1b90g4377g41b0gb07dg4a108f59fa65": (1, "I do not serve Shar anymore. Nor the Mother Superior."),
        "h6d9862b7g728fg4822ga5f3g658e9bfc16d3": (1, "What do you mean?"),
        "h78c89a38g324bg4a2cg9a76g58d634b668bf": (1, "Must I? Honestly, I'm still not used to being married - it's almost a surprise... But a very pleasant surprise."),
        "h7b905a4fgda7dg4417g9c24g768f4ef486e4": (1, "While it's a fascinating prospect, I'd like you all to myself..."),
        "h869bba83g9392g4aa0g9353gdf830a59dfd8": (1, "A scrupulous calligraphy writing is barely visible on heavily stained surface."),
        "h9635e41bge285g4f12gb61bg13692d55fba6": (1, "I didn't realize your feel this way. I want to be with you... Forget I ever said anything."),
        "h96ed575cg893bg4685g9675gaab0f31c4bbb": (1, "Bloodied piece of paper"),
        "h9a474f8dg36b3g4089gbf4aga01c55224234": (1, "Surely you wouldn't mind if I had a bit of fun? I am my own person, after all."),
        "h9b00b4fbgd0e0g4bbcgadc0gdbea99682ab5": (1, "It's difficult to put into words... I can't remember the last time I sought to confide in someone like this - maybe I never have, for all I know. But now it just feels... right."),
        "h9e23c5abg5a55g46c6g949fg4c089b18300f": (1, "You must be keen to get back to our cosy cottage, don't you?"),
        "ha0b56eb6gbc0bg4535g97efga2b7c2671c58": (1, "&lt;i&gt;Loot her belongings whlie she helplessly lies on the ground.&lt;/i&gt;"),
        "hc0077229g09edg4ed4gb446g6e6f48cf2363": (1, "Your father is right. This is the only way to free your family from Shar's curse and stop the pain."),
        "hd86ce9a8g7a59g49ddgad72g6f87d1c370dd": (1, "You're a bad liar... Don't treat me like an idiot, please!"),
        "hf070d2bag8b3cg4918ga17dg7f009caa75dc": (1, "I am free to do whatever I want. Leave, if you have a problem with that."),
        "hf278c5d2g81beg46abgaa45g649a20dfeb09": (1, "Our relationship was... fleeting. I want to move on."),
    }
    loca = bg3.loca_object(files.add_new_file(files.get_loca_relative_path()))
    loca.add_lines(content)

add_build_procedure('create_text_content', create_text_content)
