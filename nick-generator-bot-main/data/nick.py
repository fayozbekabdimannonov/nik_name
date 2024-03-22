text = "xcvbnm,"
fonts = ["🅠🅦🅔🅡🅣🅨🅤🅘🅞🅟🅐🅢🅓🅕🅖🅗🅙🅚🅛🅩🅧🅒🅥🅑🅝🅜","🅀🅆🄴🅁🅃🅈🅄🄸🄾🄿🄰🅂🄳🄵🄶🄷🄹🄺🄻🅉🅇🄲🅅🄱🄽🄼","𝕢𝕨𝕖𝕣𝕥𝕪𝕦𝕚𝕠𝕡𝕒𝕤𝕕𝕗𝕘𝕙𝕛𝕜𝕝𝕫𝕩𝕔𝕧𝕓𝕟𝕞","qωєятуυισραѕ∂ƒgнנкℓzχ¢νвηм","❀💋❀ ꝖⱲƸⱤƬƳꓴƖΘꝒ𐤠ⳜƊƑƓǶʝƘȴⱿ𐊴ƇƲƁƝ𐒄 ❀💋❀","QЩΣЯƬYЦIӨPΛƧDFGΉJKᄂZXᄃVBПM ︻╦̵̵̿╤─ ҉~•","▁▂▄▅▆▇█ QЩΣЯƬYЦIӨPΛƧDFGΉJKᄂZXᄃVBПM █▇▆▅▄▂▁","▟▛▜▟▛▜▟▛ 🅀🅆🄴🅁🅃🅈🅄🄸🄾🄿🄰🅂🄳🄵🄶🄷🄹🄺🄻🅉🅇🄲🅅🄱🄽🄼 ▟▛▜▟▛▜▟▛","(•_•)O*¯`·.¸ ợฬєгՇץยเ๏קคร๔Ŧﻮђןкɭչאςש๒ภ๓ ¸.·´¯*O(•_•)","𝒒ｗₑᵣ𝑡𝑦ᵤᵢₒ𝒑ₐ𝑠𝑑𝑓𝑔ⲏⱼⲕԼ𝑧ₓ𝑐ᵥ𝑏𝑛𝑚","♡٨ﮩ٨ﮩﮩ٨ﮩﮩ٨ﮩ ᑫᗯEᖇTYᑌIOᑭᗩᔕᗪᖴGᕼᒍKᒪᘔ᙭ᑕᐯᗷᑎᗰ ﮩ٨ﮩﮩ٨ﮩﮩ٨ﮩ٨♡"]
emoji = "⛄️✨⭐️⚽️😉😊😘😔❤️💋😒😎😀😂😛"
import random

def nick_generator(name):
    result = []
    for font in fonts:
        my_name = name
        for i in range(len(text)):
            my_name = my_name.replace(text[i],font[i])
        e = random.choice(emoji)
        result.append(e+my_name+e)
    return result

