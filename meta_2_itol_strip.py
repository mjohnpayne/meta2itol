import sys, argparse
from time import sleep as sl
import math
"""
DATASET_COLORSTRIP
SEPARATOR TAB
BORDER_WIDTH	0.5
COLOR	#bebada
DATASET_LABEL	MGT1 ST
LEGEND_COLORS	#a6cee3	#1f78b4	#b2df8a	#33a02c
LEGEND_LABELS	-	19	34	36
LEGEND_SHAPES	1	1	1	1
LEGEND_TITLE	MGT1 ST
MARGIN	5
STRIP_WIDTH	25
DATA
17-1157-0057	#1f78b4	19
17-1157-0078	#1f78b4	19
17-1157-0077	#1f78b4	19
17-1157-0085	#1f78b4	19
17-1157-0087	#33a02c	36
17-1157-0121	#1f78b4	19
17-1157-0074	#1f78b4	19
17-1157-0096	#1f78b4	19
17-1157-0104	#1f78b4	19

"""
def colnos(n):
    colourd = {
    # Dark2; colorblind-safe
    1:"#1b9e77",
    # Dark2; colorblind-safe
    2:["#1b9e77", "#d95f02"],
    # Dark2; colorblind-safe
    3:["#1b9e77", "#d95f02", "#7570b3"],
    # 4-class Paired; colorblind-safe
    4:["#a6cee3", "#1f78b4", "#b2df8a", "#33a02c"],
    # 5-class Accent; print-friendly
    5:["#a6cee3", "#1f78b4", "#b2df8a", "#33a02c",
            "#fb9a99"],
    # 6-class Paired; print-friendly
    6:["#a6cee3", "#1f78b4", "#b2df8a", "#33a02c",
            "#fb9a99", "#e31a1c"],
    # 7-class Paired; print-friendly
    7:["#a6cee3", "#1f78b4", "#b2df8a", "#33a02c",
            "#fb9a99", "#e31a1c", "#fdbf6f"],
    # Dark2; print-friendly
    8:["#1b9e77", "#d95f02", "#7570b3", "#e7298a",
            "#66a61e", "#e6ab02", "#a6761d", "#666666"],
    # 9-class Set1; print-friendly
    9:["#e41a1c", "#377eb8", "#4daf4a", "#984ea3",
            "#ff7f00", "#ffff33", "#a65628", "#f781bf", "#999999"],
    # 10-class Paired
    10:["#a6cee3", "#1f78b4", "#b2df8a", "#33a02c",
            "#fb9a99", "#e31a1c", "#fdbf6f", "#ff7f00", "#cab2d6", "#6a3d9a"],
    # 11-class Paired
    11:["#a6cee3", "#1f78b4", "#b2df8a", "#33a02c",
            "#fb9a99", "#e31a1c", "#fdbf6f", "#ff7f00", "#cab2d6", "#6a3d9a",
            "#ffff99"],
    # 12-class Paired
    12:["#a6cee3", "#1f78b4", "#b2df8a", "#33a02c",
            "#fb9a99", "#e31a1c", "#fdbf6f", "#ff7f00", "#cab2d6", "#6a3d9a",
            "#ffff99", "#b15928"],
    ## from here on: iwanthue (all colors, hard)
    13:["#8393c7", "#8ad256", "#6a49c5", "#d2b351",
            "#cb55c3", "#4d4040", "#c4527c", "#57743d", "#d85439", "#7accb1",
            "#925136", "#ceb2ab", "#512f67"],
    14:["#a2d1cd", "#5d39a8", "#71d14c", "#cb56c7",
            "#7ed094", "#4d4040", "#7077b8", "#c28b4c", "#cd9dae", "#c64a34",
            "#55868c", "#cccb51", "#b2436e", "#567137"],
    15:["#92d4ad", "#6842c1", "#6ecf58", "#cb4ec2",
            "#55733d", "#4d4040", "#c99447", "#9083cb", "#c9d14f", "#4d2c63",
            "#cea4a2", "#d54f38", "#71a6bd", "#ca507f", "#823f33"],
    16:["#76a5bd", "#bfdf44", "#cf4bab", "#66c95b",
            "#7c42c5", "#4d4040", "#7279ca", "#c27837", "#4b2a62", "#c7b956",
            "#cc8cb5", "#536e3b", "#d74746", "#84d3ae", "#893b42", "#cdb19a"],
    17:["#823f35", "#77d952", "#6d44c4", "#78d5a1",
            "#cf4a70", "#4d4040", "#ca53bd", "#69923c", "#6d7fc4", "#d1d04e",
            "#532b63", "#d64d31", "#4b623d", "#ca96b7", "#78b5c2", "#ccbf9b",
            "#c58741"],
    18:["#697bc5", "#5e9742", "#6641c0", "#7bdc57",
            "#c954c9", "#4d4040", "#4d2b62", "#73d6ac", "#d6493d", "#75adbe",
            "#c54883", "#526339", "#caca9b", "#7b332e", "#cfcf49", "#c89dc8",
            "#c58738", "#c78980"],
    19:["#9e693f", "#9147d5", "#c9d747", "#9482d3",
            "#61913d", "#4d4040", "#6dd85e", "#d049a4", "#76d0b6", "#d5493c",
            "#6897bb", "#d7993d", "#553291", "#c7cb8a", "#472f5b", "#cd7993",
            "#496340", "#ccb8bc", "#7f2c3a"],
    20:["#7295c1", "#d44b38", "#6ad14f", "#6a3bc0",
            "#cedb44", "#4d4040", "#77d192", "#cb4fc3", "#b1b85f", "#7772cc",
            "#d9973b", "#4f2b62", "#79d1cf", "#cc497b", "#4a6c2e", "#c990b5",
            "#752e30", "#d1c5ac", "#a26f47", "#537e71"],
    21:["#90b5d9", "#d6532d", "#c84ccc", "#74d147",
            "#512d79", "#4d4040", "#6740c8", "#cace49", "#6b79d1", "#6ccc84",
            "#c8478c", "#74c4b8", "#cc4458", "#4f6781", "#cb9142", "#552443",
            "#c6cb97", "#82442d", "#c489c5", "#546d37", "#cb9896"],
    22:["#392c51", "#4d4040", "#642c79", "#792d3b",
            "#6a3ec6", "#875b30", "#4f7231", "#547f72", "#d24637", "#6d71ce",
            "#d2497e", "#cd4fc8", "#6a8fbc", "#d88742", "#c78dc6", "#cc9795",
            "#c7af40", "#68cd55", "#72d4a6", "#9ecfd6", "#c9cb8f", "#c3de48"],
    23:["#8ad93f", "#c749c4", "#5e8f3d", "#6639be",
            "#73d979", "#4d4040", "#d4ca4a", "#6c6ccc", "#d78c3b", "#6485b9",
            "#d24635", "#70d4ae", "#cc4279", "#cbcb99", "#4c295f", "#ce867e",
            "#793130", "#84cbd7", "#896c35", "#c27bbb", "#364e27", "#cab2cb",
            "#5b837b"],
    24:["#ccc79a", "#6a42c7", "#d0a540", "#cc49c9",
            "#6dd755", "#4d4040", "#de5a26", "#7cc7d0", "#cc3f47", "#78d8a5",
            "#5e2d78", "#c9da51", "#6679d0", "#bf7348", "#c6b7d8", "#5f903c",
            "#c47ec5", "#6a5b29", "#ce4684", "#497359", "#772d38", "#c3858c",
            "#352444", "#5b7a9e"],
    25:["#6ba43c", "#c74ace", "#cbe14b", "#6847cd",
            "#6ede53", "#4d4040", "#cbb248", "#592e82", "#d6842f", "#5e78c1",
            "#76dd99", "#c6438e", "#4b8047", "#cf4c67", "#7acdc4", "#d2472f",
            "#7ba5c4", "#79322f", "#c388cf", "#78662f", "#45294d", "#c8cd9d",
            "#3e5d4a", "#d08c6c", "#c698a9"],
    26:["#73d991", "#b44adb", "#71d94d", "#cf4cb4",
            "#ccde4d", "#4d4040", "#ceae44", "#5a41c2", "#cdd09c", "#652e7a",
            "#83d7ce", "#dc4338", "#536e83", "#d34a79", "#5d9073", "#c68dc7",
            "#619339", "#85b1d7", "#da8340", "#6978cb", "#9d4533", "#34284e",
            "#d09e9e", "#732d41", "#364e25", "#866a38"],
    27:["#363258", "#6ed853", "#5b3fc7", "#c9de43",
            "#b54ad9", "#4d4040", "#5c2c7e", "#b7d17b", "#cf4a83", "#6ed9a4",
            "#cd4450", "#8fd3d5", "#d74527", "#769ac1", "#d27d3f", "#6d75cf",
            "#d4af42", "#4f8c3b", "#d14eba", "#568778", "#c692c8", "#344625",
            "#d4c7a6", "#722e4c", "#c88988", "#7a3a25", "#86783a"],
    28:["#7f3a27", "#71da53", "#c14bd4", "#55933d",
            "#626ad0", "#4d4040", "#623ac4", "#cbd943", "#542c79", "#c1d483",
            "#bc7fd0", "#6ad7a3", "#d84330", "#71bec7", "#ce7537", "#6f99d8",
            "#d5aa43", "#546586", "#7c7233", "#ce429f", "#3e6344", "#ce7d9f",
            "#2d1d38", "#c6b3ce", "#793151", "#bfcbae", "#d24566", "#c8927d"],
    29:["#cdc2c2", "#663dc8", "#76dd51", "#c64ece",
            "#cfda49", "#4d4040", "#549e3f", "#7577da", "#d3522e", "#7cd6ce",
            "#d4425b", "#77de9a", "#542a7e", "#d1d395", "#321e3d", "#d74a98",
            "#95963d", "#586095", "#db9a3e", "#77abd9", "#8b3c67", "#639575",
            "#d08982", "#456129", "#ca92cc", "#896134", "#597984", "#742c28",
            "#283a28"],
    30:["#31223c", "#bbe141", "#c94edb", "#65d559",
            "#8b3899", "#4d4040", "#613ec8", "#df9b36", "#6e75d5", "#c16c39",
            "#402a74", "#cfc248", "#da47a4", "#63d6ad", "#d94330", "#6abccd",
            "#c58181", "#617fae", "#7f2f2c", "#b5cfb8", "#833b65", "#b5d888",
            "#cc88cb", "#4e8a3b", "#d6466a", "#476d58", "#d2b284", "#544320",
            "#c9b6d0", "#867c36"],
    31:["#913d83", "#ced242", "#6643d0", "#79d949",
            "#c249d4", "#4d4040", "#db45a4", "#68dc88", "#3a1f4f", "#c3d483",
            "#532e8e", "#da983e", "#6d79d5", "#9b4b29", "#d085d5", "#8b7d3b",
            "#c9a0c0", "#54913d", "#dc4b32", "#72d4b1", "#8f3e58", "#90d0d8",
            "#592720", "#d2c7a9", "#21262c", "#d64769", "#3b4f25", "#6ea2cf",
            "#cd887a", "#5c6089", "#568477"],
    32:["#8f8b38", "#663cc8", "#6bd546", "#c74cce",
            "#b1d773", "#4d4040", "#c6e03a", "#59287c", "#5edb86", "#d14592",
            "#7ad9b1", "#da4627", "#719cd8", "#dc973a", "#6e71d7", "#dbc348",
            "#ca84c8", "#4c8b3a", "#d5445a", "#84ccd6", "#7f3353", "#d3c99f",
            "#2e1c38", "#ca7442", "#5a558b", "#803325", "#537286", "#cc8585",
            "#314826", "#cab3cc", "#7e6136", "#618d75"],
    33:["#d64e9e", "#6cd54c", "#dd49d1", "#c8dd41",
            "#a152dd", "#4d4040", "#5139c2", "#ceaa3b", "#432d7c", "#c6d179",
            "#8f379a", "#70d68c", "#d9432f", "#6ad5be", "#d5416a", "#76c2d7",
            "#d87a71", "#6a75d5", "#836834", "#c988d1", "#598939", "#7a3260",
            "#bed3b3", "#8f372e", "#6082b3", "#d47c35", "#312749", "#d4ac8b",
            "#314825", "#cab9d7", "#4b211f", "#ad788b", "#568275"],
    34:["#d8436c", "#653cc7", "#b4dc41", "#d143d0",
            "#5fd857", "#4d4040", "#a4db84", "#c64496", "#6adcad", "#de4830",
            "#6aa3d9", "#d98731", "#6271d1", "#dec841", "#b062cd", "#528e36",
            "#c28acd", "#675b2c", "#cbb7d3", "#a53332", "#528089", "#532878",
            "#d9d393", "#2a1e3c", "#8ed4d3", "#834629", "#5e5e8a", "#a08e3c",
            "#2b482a", "#d78763", "#619470", "#c87b8d", "#702944", "#c3a994"],
    35:["#72d4cf", "#ccdf3e", "#5533c1", "#70d951",
            "#ac42d6", "#4d4040", "#6d66dc", "#b9c866", "#562a84", "#71da99",
            "#db43c7", "#518f39", "#d04497", "#314826", "#bc6cc9", "#5d8b74",
            "#d2416d", "#72abd3", "#dd461f", "#6078c6", "#d7ab3b", "#c49ad6",
            "#7d6b2f", "#cab8c4", "#3c1a20", "#c8ddb6", "#312652", "#cfb182",
            "#7c3463", "#c98271", "#576782", "#d24243", "#cb7a99", "#82372d",
            "#cf7734"],
    36:["#6ade4b", "#6344d3", "#7bdc86", "#b746d4",
            "#65a234", "#4d4040", "#dbc941", "#552c93", "#bee148", "#dc3fb4",
            "#62d7b4", "#903a7e", "#4a8245", "#cf74d0", "#da993a", "#3e255f",
            "#c0d3b2", "#291d2d", "#cdce7e", "#752c41", "#7dcbd6", "#c43c44",
            "#669bcf", "#de4e28", "#5b5e83", "#c97449", "#bd92d0", "#847933",
            "#d7417a", "#558279", "#d07d92", "#364525", "#ceb9d0", "#763d23",
            "#6872d2", "#be9880"],
    37:["#645b8e", "#80dc40", "#4f2ea4", "#69dc7b",
            "#d848cd", "#4d4040", "#8548da", "#c7d84e", "#96368e", "#afd995",
            "#d54227", "#61d9b9", "#db4187", "#4a9339", "#cd83d6", "#7a8431",
            "#6870d5", "#e3bc3b", "#6b9bd7", "#d87935", "#6fbfcf", "#cd3e50",
            "#c3d8c8", "#772e29", "#dbc38b", "#3f2267", "#bf9340", "#cab1d6",
            "#304726", "#b2918d", "#2a1f35", "#d5816f", "#5e8c6b", "#c77192",
            "#497080", "#7d592d", "#732d52"],
    38:["#cf8ad0", "#74e042", "#b946da", "#5be080",
            "#5834c1", "#4d4040", "#d248bb", "#59a434", "#8064d4", "#b4dc4e",
            "#893876", "#96db99", "#d9478a", "#499052", "#627bcf", "#dfd238",
            "#47277a", "#908f39", "#79a2d8", "#d79234", "#4c7788", "#df502c",
            "#625984", "#d7d27b", "#2e1d3b", "#6bdac4", "#d34557", "#6a8b73",
            "#9e4427", "#cfb5cd", "#78562e", "#7cc6d5", "#26392b", "#cdcfb2",
            "#702735", "#bd7984", "#405924", "#d59571"],
    39:["#8b308f", "#74dd41", "#6939ca", "#cce346",
            "#d545d2", "#4d4040", "#b271dd", "#e39b39", "#5050bc", "#cabc46",
            "#3a1f64", "#5cde7e", "#d9428e", "#57a56d", "#d63949", "#76dfc2",
            "#7e3052", "#b7e28f", "#d286c6", "#66a234", "#6d83d8", "#d65629",
            "#76c3d2", "#843326", "#6aa0d5", "#9c762c", "#5f5488", "#d48e70",
            "#4a6a81", "#d36778", "#466b2c", "#b28491", "#273825", "#c1b47a",
            "#301b31", "#d0d2bd", "#6c552d", "#c9b8d8", "#5f8675"],
    40:["#3c2b5d", "#dee032", "#ab48d5", "#5bd749",
            "#db49c6", "#4d4040", "#5c42d0", "#a4e040", "#462687", "#d8b136",
            "#8d3989", "#60d076", "#d7468f", "#63d8b5", "#de4528", "#77c7d6",
            "#d13a55", "#5f8c7b", "#ce88d5", "#759b31", "#696ecd", "#de8739",
            "#6f9ad6", "#b75738", "#aadc90", "#946d89", "#d0dc6a", "#2c1a25",
            "#c6d8bc", "#782849", "#ceb977", "#283f27", "#d9798c", "#447c3d",
            "#ceb8d4", "#635b2d", "#c79783", "#733426", "#476682", "#98762e"]
    }
    if n <= 40:
        return colourd[n]
    else:
        whole = math.floor(float(n)/40)
        r = n%40
        comb = whole*colourd[40] + colourd[r]
        return comb

def collist1():
    colourlist = ["#FFFF00", "#1CE6FF", "#FF34FF", "#FF4A46", "#008941", "#006FA6", "#A30059", "#FFDBE5", "#7A4900",
                  "#0000A6", "#63FFAC", "#B79762", "#004D43", "#8FB0FF", "#997D87", "#5A0007", "#809693", "#FEFFE6",
                  "#1B4400", "#4FC601", "#3B5DFF", "#4A3B53", "#FF2F80", "#61615A", "#BA0900", "#6B7900", "#00C2A0",
                  "#FFAA92", "#FF90C9", "#B903AA", "#D16100", "#DDEFFF", "#000035", "#7B4F4B", "#A1C299", "#300018",
                  "#0AA6D8", "#013349", "#00846F", "#372101", "#FFB500", "#C2FFED", "#A079BF", "#CC0744", "#C0B9B2",
                  "#C2FF99", "#001E09", "#00489C", "#6F0062", "#0CBD66", "#EEC3FF", "#456D75", "#B77B68", "#7A87A1",
                  "#788D66", "#885578", "#FAD09F", "#FF8A9A", "#D157A0", "#BEC459", "#456648", "#0086ED", "#886F4C",
                  "#34362D", "#B4A8BD", "#00A6AA", "#452C2C", "#636375", "#A3C8C9", "#FF913F", "#938A81", "#575329",
                  "#00FECF", "#B05B6F", "#8CD0FF", "#3B9700", "#04F757", "#C8A1A1", "#1E6E00", "#7900D7", "#A77500",
                  "#6367A9", "#A05837", "#6B002C", "#772600", "#D790FF", "#9B9700", "#549E79", "#FFF69F", "#201625",
                  "#72418F", "#BC23FF", "#99ADC0", "#3A2465", "#922329", "#5B4534", "#FDE8DC", "#404E55", "#0089A3",
                  "#CB7E98", "#A4E804", "#324E72", "#6A3A4C", "#83AB58", "#001C1E", "#D1F7CE", "#004B28", "#C8D0F6",
                  "#A3A489", "#806C66", "#222800", "#BF5650", "#E83000", "#66796D", "#DA007C", "#FF1A59", "#8ADBB4",
                  "#1E0200", "#5B4E51", "#C895C5", "#320033", "#FF6832", "#66E1D3", "#CFCDAC", "#D0AC94", "#7ED379",
                  "#012C58", "#7A7BFF", "#D68E01", "#353339", "#78AFA1", "#FEB2C6", "#75797C", "#837393", "#943A4D",
                  "#B5F4FF", "#D2DCD5", "#9556BD", "#6A714A", "#001325", "#02525F", "#0AA3F7", "#E98176", "#DBD5DD",
                  "#5EBCD1", "#3D4F44", "#7E6405", "#02684E", "#962B75", "#8D8546", "#9695C5", "#E773CE", "#D86A78",
                  "#3E89BE", "#CA834E", "#518A87", "#5B113C", "#55813B", "#E704C4", "#00005F", "#A97399", "#4B8160",
                  "#59738A", "#FF5DA7", "#F7C9BF", "#643127", "#513A01", "#6B94AA", "#51A058", "#A45B02", "#1D1702",
                  "#E20027", "#E7AB63", "#4C6001", "#9C6966", "#64547B", "#97979E", "#006A66", "#391406", "#F4D749",
                  "#0045D2", "#006C31", "#DDB6D0", "#7C6571", "#9FB2A4", "#00D891", "#15A08A", "#BC65E9", "#FFFFFE",
                  "#C6DC99", "#203B3C", "#671190", "#6B3A64", "#F5E1FF", "#FFA0F2", "#CCAA35", "#374527", "#8BB400",
                  "#797868", "#C6005A", "#3B000A", "#C86240", "#29607C", "#402334", "#7D5A44", "#CCB87C", "#B88183",
                  "#AA5199", "#B5D6C3", "#A38469", "#9F94F0", "#A74571", "#B894A6", "#71BB8C", "#00B433", "#789EC9",
                  "#6D80BA", "#953F00", "#5EFF03", "#E4FFFC", "#1BE177", "#BCB1E5", "#76912F", "#003109", "#0060CD",
                  "#D20096", "#895563", "#29201D", "#5B3213", "#A76F42", "#89412E", "#1A3A2A", "#494B5A", "#A88C85",
                  "#F4ABAA", "#A3F3AB", "#00C6C8", "#EA8B66", "#958A9F", "#BDC9D2", "#9FA064", "#BE4700", "#658188",
                  "#83A485", "#453C23", "#47675D", "#3A3F00", "#061203", "#DFFB71", "#868E7E", "#98D058", "#6C8F7D",
                  "#D7BFC2", "#3C3E6E", "#D83D66", "#2F5D9B", "#6C5E46", "#D25B88", "#5B656C", "#00B57F", "#545C46",
                  "#866097", "#365D25", "#252F99", "#00CCFF", "#674E60", "#FC009C", "#92896B"]
    return colourlist
def collist2():
    colourlist2 = ["#FFFF00", "#1CE6FF", "#FF34FF", "#FF4A46", "#008941", "#006FA6", "#A30059", "#FFDBE5", "#7A4900",
                   "#0000A6", "#63FFAC", "#B79762", "#004D43", "#8FB0FF", "#997D87", "#5A0007", "#809693", "#FEFFE6",
                   "#1B4400", "#4FC601", "#3B5DFF", "#4A3B53", "#FF2F80", "#61615A", "#BA0900", "#6B7900", "#00C2A0",
                   "#FFAA92", "#FF90C9", "#B903AA", "#D16100", "#DDEFFF", "#000035", "#7B4F4B", "#A1C299", "#300018",
                   "#0AA6D8", "#013349", "#00846F", "#372101", "#FFB500", "#C2FFED", "#A079BF", "#CC0744", "#C0B9B2",
                   "#C2FF99", "#001E09", "#00489C", "#6F0062", "#0CBD66", "#EEC3FF", "#456D75", "#B77B68", "#7A87A1",
                   "#788D66", "#885578", "#FAD09F", "#FF8A9A", "#D157A0", "#BEC459", "#456648", "#0086ED", "#886F4C",
                   "#34362D", "#B4A8BD", "#00A6AA", "#452C2C", "#636375", "#A3C8C9", "#FF913F", "#938A81", "#575329",
                   "#00FECF", "#B05B6F", "#8CD0FF", "#3B9700", "#04F757", "#C8A1A1", "#1E6E00", "#7900D7", "#A77500",
                   "#6367A9", "#A05837", "#6B002C", "#772600", "#D790FF", "#9B9700", "#549E79", "#FFF69F", "#201625",
                   "#72418F", "#BC23FF", "#99ADC0", "#3A2465", "#922329", "#5B4534", "#FDE8DC", "#404E55", "#0089A3",
                   "#CB7E98", "#A4E804", "#324E72", "#6A3A4C", "#83AB58", "#001C1E", "#D1F7CE", "#004B28", "#C8D0F6",
                   "#A3A489", "#806C66", "#222800", "#BF5650", "#E83000", "#66796D", "#DA007C", "#FF1A59", "#8ADBB4",
                   "#1E0200", "#5B4E51", "#C895C5", "#320033", "#FF6832", "#66E1D3", "#CFCDAC", "#D0AC94", "#7ED379",
                   "#012C58", "#7A7BFF", "#D68E01", "#353339", "#78AFA1", "#FEB2C6", "#75797C", "#837393", "#943A4D",
                   "#B5F4FF", "#D2DCD5", "#9556BD", "#6A714A", "#001325", "#02525F", "#0AA3F7", "#E98176", "#DBD5DD",
                   "#5EBCD1", "#3D4F44", "#7E6405", "#02684E", "#962B75", "#8D8546", "#9695C5", "#E773CE", "#D86A78",
                   "#3E89BE", "#CA834E", "#518A87", "#5B113C", "#55813B", "#E704C4", "#00005F", "#A97399", "#4B8160",
                   "#59738A", "#FF5DA7", "#F7C9BF", "#643127", "#513A01", "#6B94AA", "#51A058", "#A45B02", "#1D1702",
                   "#E20027", "#E7AB63", "#4C6001", "#9C6966", "#64547B", "#97979E", "#006A66", "#391406", "#F4D749",
                   "#0045D2", "#006C31", "#DDB6D0", "#7C6571", "#9FB2A4", "#00D891", "#15A08A", "#BC65E9", "#FFFFFE",
                   "#C6DC99", "#203B3C", "#671190", "#6B3A64", "#F5E1FF", "#FFA0F2", "#CCAA35", "#374527", "#8BB400",
                   "#797868", "#C6005A", "#3B000A", "#C86240", "#29607C", "#402334", "#7D5A44", "#CCB87C", "#B88183",
                   "#AA5199", "#B5D6C3", "#A38469", "#9F94F0", "#A74571", "#B894A6", "#71BB8C", "#00B433", "#789EC9",
                   "#6D80BA", "#953F00", "#5EFF03", "#E4FFFC", "#1BE177", "#BCB1E5", "#76912F", "#003109", "#0060CD",
                   "#D20096", "#895563", "#29201D", "#5B3213", "#A76F42", "#89412E", "#1A3A2A", "#494B5A", "#A88C85",
                   "#F4ABAA", "#A3F3AB", "#00C6C8", "#EA8B66", "#958A9F", "#BDC9D2", "#9FA064", "#BE4700", "#658188",
                   "#83A485", "#453C23", "#47675D", "#3A3F00", "#061203", "#DFFB71", "#868E7E", "#98D058", "#6C8F7D",
                   "#D7BFC2", "#3C3E6E", "#D83D66", "#2F5D9B", "#6C5E46", "#D25B88", "#5B656C", "#00B57F", "#545C46",
                   "#866097", "#365D25", "#252F99", "#00CCFF", "#674E60", "#FC009C", "#92896B"]
    return colourlist2

def parseargs():
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-m", "--metadata", help="input metadata file",required=True)
    parser.add_argument("-o", "--outputprefix", help="output prefix, each colum name will be appended to this to "
                                                     "generate ouput files",required=True)
    parser.add_argument("-c", "--columns", help="list (comma separated) of columns to generate colour strips for", default="all")
    parser.add_argument("-t", "--tip_id", help="column header with strain ids matching tree tips", default="Strain")
    parser.add_argument("-s", "--sep", help="delimiter between columns", default="\t")

    args = parser.parse_args()
    return args

def get_strain_to_meta(args):
    outdict = {}

    inf = open(args.metadata,"r").read().splitlines()
    header = inf[0].split(args.sep)
    if args.tip_id not in header:
        sys.exit("tip id {} not in metadata header".format(args.tip_id))

    straincol = header.index(args.tip_id)

    metadata_cols = []
    if args.columns == "all":
        metadata_cols = [header.index(x) for x in header if x != args.tip_id]
    else:
        colids = args.columns.split(",")
        notheader = []
        for i in colids:
            if i not in header:
                notheader.append(i)
        if notheader != []:
            sys.exit("following column names not in metadata file: " + ",".join(notheader))
        metadata_cols = [header.index(x) for x in colids if x != args.tip_id]
    straindupes = []
    for row in inf[1:]:
        col = row.split(args.sep)
        strain = col[straincol]
        for colno in metadata_cols:
            metaid = header[colno]
            if metaid not in outdict:
                outdict[metaid] = {strain:col[colno]}
            elif strain in outdict[metaid]:
                straindupes.append(strain)
            else:
                outdict[metaid][strain] = col[colno]
    if straindupes != []:
        sys.exit("following strain ids duplicated: {}".format(",".join(straindupes)))

    return outdict


def make_meta_to_colour(strain_to_meta):
    metacols = {}
    for metatype in strain_to_meta:
        values = list(set(strain_to_meta[metatype].values()))
        colours = colnos(len(values))
        metacols[metatype] = dict(zip(values,colours))
    return metacols

def get_meta_and_col_lists(type_to_colour):
    types = sorted(list(type_to_colour.keys()))
    colours = []
    for i in types:
        colours.append(type_to_colour[i])
    return types,colours


def generate_outputs(args,strain_to_meta,metadata_colours):
    outheader = "DATASET_COLORSTRIP\nSEPARATOR TAB\nBORDER_WIDTH\t0.5\nCOLOR\t#bebada"

    for metatype in strain_to_meta:
        outfile = outheader + "\nDATASET_LABEL\t {}\n".format(metatype)

        strain_to_type = strain_to_meta[metatype]
        type_to_colour = metadata_colours[metatype]
        types,colours = get_meta_and_col_lists(type_to_colour)
        outfile += "LEGEND_COLORS\t{}\n".format("\t".join(colours))
        outfile += "LEGEND_LABELS\t{}\n".format("\t".join(types))
        outfile += "LEGEND_SHAPES\t{}\n".format( "\t".join(["1"]*len(types)))
        outfile += "LEGEND_TITLE\t{}\n".format(metatype)
        outfile += "MARGIN\t5\nSTRIP_WIDTH\t25\n DATA\n"
        for strain in sorted(list(strain_to_type.keys())):
            meta = strain_to_type[strain]
            colour = type_to_colour[meta]
            outfile += "{}\t{}\t{}\n".format(strain,colour,meta)
        outf = open("{}_{}_itol_colourstrip.txt".format(args.outputprefix,metatype),"w")
        outf.write(outfile)
        outf.close()

def main():
    args = parseargs()
    strain_to_meta = get_strain_to_meta(args) # strain_to_meta straucture = {metadata_type:{strain_id:strain_value}}
    metadata_colours = make_meta_to_colour(strain_to_meta) # metadata_colours straucture = {metadata_type:{meta_value:meta_colour}}
    generate_outputs(args,strain_to_meta,metadata_colours)

if __name__ == '__main__':
    main()
