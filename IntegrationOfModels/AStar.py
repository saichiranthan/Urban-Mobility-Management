from PredictTime import get_predicted_times, ward_names_to_ids
from TrafficDensity import get_traffic_density
from itertools import combinations
import folium
import heapq
import math

wards ={
    "Kempegowda Ward": (13.109589249219718, 77.57643348397863),
    "Chowdeshwari Ward": (13.110331859835348, 77.5904830143365),
    "Atturu Ward": (13.100420837576957, 77.5766418644281),
    "Yelahanka Satellite Town Ward": (13.104261592495142, 77.57134446723518),
    "Kogilu Ward": (13.101069084893155, 77.61234022732434),
    "Jakkuru Ward": (13.079165785378777, 77.6073620475339),
    "Thanisandra Ward": (13.056036948969673, 77.63248172441142),
    "Amrutahalli Ward": (13.065986568054784, 77.60398593664537),
    "Hebbal Kempapura Ward": (13.052863090482939, 77.60144366724452),
    "Byatarayanapura Ward": (13.06172590976814, 77.58732451939058),
    "Kodigehalli": (13.069668177615773, 77.5787572872883),
    "Dodda Bommasandra": (13.060554812278594, 77.56202030351005),
    "Vidyaranyapura": (13.081846883890568, 77.55572259715204),
    "Kuvempu Nagar": (13.347894832393605, 77.12862910340571),
    "Kammagondanahalli": (13.05925801270911, 77.53510846862007),
    "Mallasandra": (13.06101383407049, 77.51184835270261),
    "Chikkasandra": (13.066370062748284, 77.51191332753618),
    "Bagalakunte": (13.052970780408673, 77.49558964840988),
    "T Dasarahalli": (13.050914079474722, 77.51558482950702),
    "Nalagadarenahalli": (13.035152401926409, 77.50893295133872),
    "Chokkasandra": (13.039019296655976, 77.51545925314349),
    "Peenya Industrial Area": (13.028566865468708, 77.51970787210257),
    "Rajagopal Nagar": (13.012619188672087, 77.51177735098699),
    "Hegganahalli": (13.006368021723336, 77.5170773958501),
    "Sunkadakatte": (12.992208457621421, 77.50514294017705),
    "Dodda Bidarakallu": (13.033185476518453, 77.48986507806154),
    "Lingadheeranahalli": (12.874889244086269, 77.51412115154909),
    "Herohalli": (12.989996520319819, 77.48905859122475),
    "Ullalu": (12.958563471833493, 77.47924280527616),
    "Nagadevanahalli": (12.942252203105205, 77.49065828651979),
    "Bande Mutt": (12.92034840034914, 77.47826505629318),
    "Kengeri": (12.8996841157615, 77.48298574402551),
    "Hemmigepura": (12.885167791871693, 77.48942413480445),
    "JP Park": (13.034389328426943, 77.55053558326655),
    "Yeshwanthpura": (13.024763041943535, 77.53391731803252),
    "Jalahalli": (13.045835014899342, 77.54799355054345),
    "Peenya": (13.028659707742696, 77.51962602750554),
    "Laxmidevi Nagar": (13.013941942207065, 77.52683580513309),
    "Laggere": (13.00970307599769, 77.52541104963494),
    "Chowdeshwari Nagar": (13.001904681487021, 77.52317945179784),
    "Kottegepalya": (12.985585039628036, 77.51152083977493),
    "Srigandhadakaval": (12.974586700830567, 77.50478313092063),
    "Malathalli": (12.961924181625392, 77.49797471268396),
    "Jnana Bharathi": (12.941681277812739, 77.51006325397071),
    "Rajarajeshwari Nagar": (12.914995353745672, 77.52070625903995),
    "Rajiv Nagar": (12.92098347311362, 77.555266934532),
    "Mahalakshmipuram": (13.014662145236866, 77.55114706160197),
    "Nagapura": (13.00176100399789, 77.54418328601086),
    "Nalvadi Krishna Raja Wadiyar": (12.970815880501933, 77.59190514745036),
    "Shankar Matt": (12.955252628542448, 77.57057216760523),
    "Shakthi Ganapathi Nagar": (12.992305005899457, 77.53718403069094),
    "Vrisabhavathi Nagar": (12.987515028238011, 77.52058404084518),
    "Mattikere": (13.03317556781556, 77.5636710452384),
    "Malleswaram": (13.005460584552841, 77.56924916937339),
    "Aramane Nagara": (13.014492353321822, 77.58396913202965),
    "Rajamahal Guttahalli": (13.00002080995799, 77.58396112516716),
    "Kadu Malleshwara": (13.005122239054641, 77.5716444217201),
    "Subramanya Nagar": (13.006402774704943, 77.55764456289933),
    "Gayithri Nagar": (13.000653235388087, 77.55768747824234),
    "Radhakrishna Temple": (13.033608328534704, 77.57563124664856),
    "Sanjaya Nagar": (13.036917037209628, 77.57849818939147),
    "Hebbala": (13.035397294420722, 77.59878328013792),
    "Vishwanath Nagenahalli": (13.038804741445952, 77.60401895198649),
    "Manorayanapalya": (13.030156762508048, 77.60410788527818),
    "Chamundi Nagara": (13.031735097773463, 77.59991291049785),
    "Ganga Nagar": (13.020462287184024, 77.58879912764704),
    "Jayachamarajendra Nagar": (12.986687294959335, 77.54670005663732),
    "Kaval Bairasandra": (13.023662550692134, 77.60803066378475),
    "Kushal Nagar": (13.019899492923381, 77.61712871650523),
    "Muneshwara Nagar": (12.895391998468343, 77.6422921384822),
    "Devara Jeevanahalli": (13.011158828806094, 77.60898983229784),
    "S K Garden": (13.004880096146058, 77.60672445901298),
    "Sagayarapuram": (13.007096260233515, 77.6171314296956),
    "Pulikeshinagar": (12.996816393216948, 77.61459928439525),
    "Hennur": (13.036454757256028, 77.64343839490546),
    "Nagavara": (13.042081007810463, 77.61359823869783),
    "HBR Layout": (13.035266157076121, 77.62848986272617),
    "Kadugondanahalli": (13.018657820756625, 77.61872650746372),
    "Kacharkanahalli": (13.015647318309233, 77.63207317914329),
    "Kammanahalli": (13.01588958592286, 77.63787563202824),
    "Banasavadi": (13.010349335027962, 77.64811094133877),
    "Subbayyanapalya": (13.012790332900282, 77.6457916615389),
    "Lingarajapura": (13.01312483883325, 77.62622226462497),
    "Begur":(12.87618038363489, 77.63746384753141)
}



distances = {
'Kempegowda Ward': {'Yelahanka Satellite Town Ward': 0.8091311004888314, 'Atturu Ward': 1.0197306071570826, 'Chowdeshwari Ward': 1.523758283411514, 'Vidyaranyapura': 3.814097450189065, 'Kogilu Ward': 4.002403212137341, 'Kodigehalli': 4.446149749000907, 'Jakkuru Ward': 4.760733246327759, 'Byatarayanapura Ward': 5.451312061193934, 'Dodda Bommasandra': 5.671451299898484, 'Amrutahalli Ward': 5.693142561672254},
'Chowdeshwari Ward': {'Kempegowda Ward': 1.523758283411514, 'Atturu Ward': 1.860502019995477, 'Yelahanka Satellite Town Ward': 2.1798041029098467, 'Kogilu Ward': 2.5814806640064827, 'Jakkuru Ward': 3.918105688628096, 'Kodigehalli': 4.696554637439182, 'Vidyaranyapura': 4.919852377815378, 'Amrutahalli Ward': 5.14327207849488, 'Byatarayanapura Ward': 5.415550320924318, 'Dodda Bommasandra': 6.335529703260981},
'Atturu Ward': {'Yelahanka Satellite Town Ward': 0.7152152400927752, 'Kempegowda Ward': 1.0197306071570826, 'Chowdeshwari Ward': 1.860502019995477, 'Vidyaranyapura': 3.0657485964587257, 'Kodigehalli': 3.427206835798253, 'Kogilu Ward': 3.866835245183647, 'Jakkuru Ward': 4.081173317165116, 'Byatarayanapura Ward': 4.455533383407405, 'Dodda Bommasandra': 4.7072892580024615, 'Amrutahalli Ward': 4.8406256679362105},
'Yelahanka Satellite Town Ward': {'Atturu Ward': 0.7152152400927752, 'Kempegowda Ward': 0.8091311004888314, 'Chowdeshwari Ward': 2.1798041029098467, 'Vidyaranyapura': 3.0124147615011414, 'Kodigehalli': 3.9295049690522226, 'Kogilu Ward': 4.4540105291875625, 'Jakkuru Ward': 4.79623664200693, 'Dodda Bommasandra': 4.963789673873715, 'Byatarayanapura Ward': 5.036481676478607, 'Amrutahalli Ward': 5.532806599287344},
'Kogilu Ward': {'Jakkuru Ward': 2.4945005120707147, 'Chowdeshwari Ward': 2.5814806640064827, 'Atturu Ward': 3.866835245183647, 'Kempegowda Ward': 4.002403212137341, 'Amrutahalli Ward': 4.004562405364014, 'Yelahanka Satellite Town Ward': 4.4540105291875625, 'Kodigehalli': 5.0419526716109635, 'Byatarayanapura Ward': 5.145831104308302, 'Thanisandra Ward': 5.461923810673187, 'Hebbal Kempapura Ward': 5.4886546275109},
'Jakkuru Ward': {'Amrutahalli Ward': 1.5103970367335167, 'Kogilu Ward': 2.4945005120707147, 'Byatarayanapura Ward': 2.9104995816723855, 'Hebbal Kempapura Ward': 2.994157020386053, 'Kodigehalli': 3.2732975342186834, 'Thanisandra Ward': 3.743957603349301, 'Chowdeshwari Ward': 3.918105688628096, 'Atturu Ward': 4.081173317165116, 'Nagavara': 4.17859937636028, 'Vishwanath Nagenahalli': 4.50252897431082},
'Thanisandra Ward': {'HBR Layout': 2.349738039885597, 'Hennur': 2.4799048791399105, 'Nagavara': 2.5675578650272883, 'Amrutahalli Ward': 3.2789022309946647, 'Hebbal Kempapura Ward': 3.3805512957408976, 'Vishwanath Nagenahalli': 3.6301167128677116, 'Jakkuru Ward': 3.743957603349301, 'Manorayanapalya': 4.210536130527267, 'Hebbala': 4.311895847901597, 'Kushal Nagar': 4.348893332302543},
'Amrutahalli Ward': {'Hebbal Kempapura Ward': 1.4850197922061874, 'Jakkuru Ward': 1.5103970367335167, 'Byatarayanapura Ward': 1.8658646772532863, 'Kodigehalli': 2.7631432946286103, 'Nagavara': 2.8548273856779223, 'Vishwanath Nagenahalli': 3.0224833316207413, 'Thanisandra Ward': 3.2789022309946647, 'Hebbala': 3.447744035483273, 'Chamundi Nagara': 3.8340601910573366, 'Manorayanapalya': 3.984114499375971},
'Hebbal Kempapura Ward': {'Amrutahalli Ward': 1.4850197922061874, 'Vishwanath Nagenahalli': 1.5879139164787193, 'Nagavara': 1.7807075225521938, 'Byatarayanapura Ward': 1.819403908921631, 'Hebbala': 1.9633735380319635, 'Chamundi Nagara': 2.3551703876397805, 'Manorayanapalya': 2.5412698508626703, 'Jakkuru Ward': 2.994157020386053, 'Sanjaya Nagar': 3.0532033988769394, 'Kodigehalli': 3.087130602220877},
'Byatarayanapura Ward': {'Kodigehalli': 1.2810407162719635, 'Hebbal Kempapura Ward': 1.819403908921631, 'Amrutahalli Ward': 1.8658646772532863, 'Dodda Bommasandra': 2.7440001149360227, 'Jakkuru Ward': 2.9104995816723855, 'Sanjaya Nagar': 2.919608301633805, 'Vishwanath Nagenahalli': 3.1250985465569676, 'Hebbala': 3.1798754758193772, 'Radhakrishna Temple': 3.373372536997899, 'Nagavara': 3.5876939167015283},
'Kodigehalli': {'Byatarayanapura Ward': 1.2810407162719635, 'Dodda Bommasandra': 2.0768906610207707, 'Amrutahalli Ward': 2.7631432946286103, 'Vidyaranyapura': 2.83876024199467, 'Hebbal Kempapura Ward': 3.087130602220877, 'Jakkuru Ward': 3.2732975342186834, 'Atturu Ward': 3.427206835798253, 'Sanjaya Nagar': 3.641868801074958, 'Yelahanka Satellite Town Ward': 3.9295049690522226, 'Radhakrishna Temple': 4.023945257471543},
'Dodda Bommasandra': {'Kodigehalli': 2.0768906610207707, 'Jalahalli': 2.233291010843793, 'Vidyaranyapura': 2.4638768150587627, 'Byatarayanapura Ward': 2.7440001149360227, 'Kammagondanahalli': 2.918621829963829, 'Mattikere': 3.049679960784608, 'JP Park': 3.1642897209632723, 'Sanjaya Nagar': 3.1771874700773988, 'Radhakrishna Temple': 3.3394213846381744, 'Hebbal Kempapura Ward': 4.355153753303377},
'Vidyaranyapura': {'Dodda Bommasandra': 2.4638768150587627, 'Kodigehalli': 2.83876024199467, 'Yelahanka Satellite Town Ward': 3.0124147615011414, 'Atturu Ward': 3.0657485964587257, 'Kammagondanahalli': 3.360711143217585, 'Kempegowda Ward': 3.814097450189065, 'Byatarayanapura Ward': 4.089266404955522, 'Jalahalli': 4.09091665078706, 'Chowdeshwari Ward': 4.919852377815378, 'Chikkasandra': 5.0475308911463905},
'Kuvempu Nagar': {'Bagalakunte': 51.513107138659535, 'Chikkasandra': 51.97624599101474, 'Mallasandra': 52.33189650797742, 'Dodda Bidarakallu': 52.47861499072178, 'T Dasarahalli': 53.34168046742556, 'Nalagadarenahalli': 53.89299041686425, 'Chokkasandra': 54.16073170038887, 'Kammagondanahalli': 54.46464905689722, 'Vidyaranyapura': 54.88766174732613, 'Yelahanka Satellite Town Ward': 55.04922544824319},
'Kammagondanahalli': {'Jalahalli': 2.04348914999585, 'T Dasarahalli': 2.309388463899992, 'Mallasandra': 2.527058664483008, 'Chikkasandra': 2.6339624104431993, 'Dodda Bommasandra': 2.918621829963829, 'Chokkasandra': 3.097561151831502, 'JP Park': 3.231008906552155, 'Vidyaranyapura': 3.360711143217585, 'Peenya': 3.7932819929215356, 'Peenya Industrial Area': 3.7986425468110756},
'Mallasandra': {'Chikkasandra': 0.5956270359678736, 'T Dasarahalli': 1.1937479999106804, 'Bagalakunte': 1.9752175725359944, 'Chokkasandra': 2.476761814872825, 'Kammagondanahalli': 2.527058664483008, 'Nalagadarenahalli': 2.892949245234044, 'Peenya': 3.6949521028919357, 'Peenya Industrial Area': 3.7070306710849894, 'Dodda Bidarakallu': 3.9045933100252466, 'Jalahalli': 4.263604541346718},
'Chikkasandra': {'Mallasandra': 0.5956270359678736, 'T Dasarahalli': 1.7640406998330669, 'Bagalakunte': 2.3122063520098886, 'Kammagondanahalli': 2.6339624104431993, 'Chokkasandra': 3.065425832031477, 'Nalagadarenahalli': 3.486226149911476, 'Peenya': 4.275621761159664, 'Peenya Industrial Area': 4.287483974042619, 'Dodda Bidarakallu': 4.395445849901884, 'Jalahalli': 4.526380255101058},
'Bagalakunte': {'Mallasandra': 1.9752175725359944, 'T Dasarahalli': 2.177963943971865, 'Dodda Bidarakallu': 2.285751869569696, 'Chikkasandra': 2.3122063520098886, 'Nalagadarenahalli': 2.4525192047866673, 'Chokkasandra': 2.653176683838208, 'Peenya': 3.753317733917175, 'Peenya Industrial Area': 3.766904170382751, 'Kammagondanahalli': 4.337408992727354, 'Rajagopal Nagar': 4.817406132752604},
'T Dasarahalli': {'Mallasandra': 1.1937479999106804, 'Chokkasandra': 1.3227094538315338, 'Chikkasandra': 1.7640406998330669, 'Nalagadarenahalli': 1.8949661689448576, 'Bagalakunte': 2.177963943971865, 'Kammagondanahalli': 2.309388463899992, 'Peenya': 2.512997844590154, 'Peenya Industrial Area': 2.524717609070568, 'Dodda Bidarakallu': 3.413017149731034, 'Yeshwanthpura': 3.521304408499435},
'Nalagadarenahalli': {'Chokkasandra': 0.8274731339434067, 'Peenya': 1.3649510002944252, 'Peenya Industrial Area': 1.3779421594862575, 'T Dasarahalli': 1.8949661689448576, 'Dodda Bidarakallu': 2.077170628718525, 'Bagalakunte': 2.4525192047866673, 'Rajagopal Nagar': 2.5244564875790223, 'Mallasandra': 2.892949245234044, 'Yeshwanthpura': 2.942838028896588, 'Laxmidevi Nagar': 3.0535443930496613},
'Chokkasandra': {'Nalagadarenahalli': 0.8274731339434067, 'Peenya': 1.2372154422557975, 'Peenya Industrial Area': 1.2500702872286042, 'T Dasarahalli': 1.3227094538315338, 'Mallasandra': 2.476761814872825, 'Yeshwanthpura': 2.5517171276255843, 'Bagalakunte': 2.653176683838208, 'Dodda Bidarakallu': 2.8474717318888003, 'Rajagopal Nagar': 2.962533002562301, 'Laxmidevi Nagar': 3.048696529619048},
'Peenya Industrial Area': {'Peenya': 0.013608456520094807, 'Chokkasandra': 1.2500702872286042, 'Nalagadarenahalli': 1.3779421594862575, 'Yeshwanthpura': 1.5964084558405618, 'Laxmidevi Nagar': 1.8002473518729682, 'Rajagopal Nagar': 1.9704703012964726, 'Laggere': 2.1866648350683557, 'Hegganahalli': 2.4847948841014715, 'T Dasarahalli': 2.524717609070568, 'Chowdeshwari Nagar': 2.988460943095574},
'Rajagopal Nagar': {'Hegganahalli': 0.9015986153836999, 'Laggere': 1.5122493906955208, 'Laxmidevi Nagar': 1.6380378421687323, 'Chowdeshwari Nagar': 1.7162336439538897, 'Peenya Industrial Area': 1.9704703012964726, 'Peenya': 1.9759341882741304, 'Sunkadakatte': 2.3806759129650032, 'Nalagadarenahalli': 2.5244564875790223, 'Yeshwanthpura': 2.7525555458495687, 'Vrisabhavathi Nagar': 2.9500245843474704},
'Hegganahalli': {'Chowdeshwari Nagar': 0.8266735802932185, 'Rajagopal Nagar': 0.9015986153836999, 'Laggere': 0.9760719257434406, 'Laxmidevi Nagar': 1.3516687824651614, 'Sunkadakatte': 2.0373806103716747, 'Vrisabhavathi Nagar': 2.1305074680644087, 'Kottegepalya': 2.3880938276423604, 'Peenya Industrial Area': 2.4847948841014715, 'Peenya': 2.4940534356819266, 'Shakthi Ganapathi Nagar': 2.6815956739184514},
'Sunkadakatte': {'Kottegepalya': 1.0099310389547935, 'Vrisabhavathi Nagar': 1.752543555750348, 'Herohalli': 1.7599921102663938, 'Srigandhadakaval': 1.9598377586973654, 'Hegganahalli': 2.0373806103716747, 'Chowdeshwari Nagar': 2.231884357468964, 'Rajagopal Nagar': 2.3806759129650032, 'Laggere': 2.9336657017558148, 'Laxmidevi Nagar': 3.3710606560826517, 'Malathalli': 3.4558726830191984},
'Dodda Bidarakallu': {'Nalagadarenahalli': 2.077170628718525, 'Bagalakunte': 2.285751869569696, 'Chokkasandra': 2.8474717318888003, 'Peenya': 3.263087335343631, 'Peenya Industrial Area': 3.273452254844016, 'Rajagopal Nagar': 3.2962099884035028, 'T Dasarahalli': 3.413017149731034, 'Mallasandra': 3.9045933100252466, 'Hegganahalli': 4.193245981663446, 'Chikkasandra': 4.395445849901884},
'Lingadheeranahalli': {'Hemmigepura': 2.9108523899771943, 'Kengeri': 4.3579001949695, 'Rajarajeshwari Nagar': 4.516354204775913, 'Bande Mutt': 6.37617303607132, 'Rajiv Nagar': 6.794092734077727, 'Jnana Bharathi': 7.439946565385214, 'Nagadevanahalli': 7.910329868528543, 'Malathalli': 9.834785814391243, 'Ullalu': 10.042748472162213, 'Shankar Matt': 10.829836273502316},
'Herohalli': {'Sunkadakatte': 1.7599921102663938, 'Srigandhadakaval': 2.4163990862865594, 'Kottegepalya': 2.4827340132140687, 'Malathalli': 3.267589698477601, 'Vrisabhavathi Nagar': 3.42690654275634, 'Rajagopal Nagar': 3.519462014661402, 'Hegganahalli': 3.5397108075534156, 'Ullalu': 3.653442195763154, 'Chowdeshwari Nagar': 3.926865523121049, 'Laggere': 4.507139520349198},
'Ullalu': {'Malathalli': 2.0639453153371727, 'Nagadevanahalli': 2.1954334290291433, 'Srigandhadakaval': 3.291463697130331, 'Herohalli': 3.653442195763154, 'Jnana Bharathi': 3.8313108770191566, 'Bande Mutt': 4.250642960827793, 'Kottegepalya': 4.610953689453031, 'Sunkadakatte': 4.676778399381502, 'Vrisabhavathi Nagar': 5.516385921583447, 'Kengeri': 6.5596400906494585},
'Nagadevanahalli': {'Jnana Bharathi': 2.1038799285799508, 'Ullalu': 2.1954334290291433, 'Malathalli': 2.326679475702115, 'Bande Mutt': 2.781378429591243, 'Srigandhadakaval': 3.9076727326602274, 'Rajarajeshwari Nagar': 4.44865850001867, 'Kengeri': 4.805842374509415, 'Herohalli': 5.3117550159101175, 'Kottegepalya': 5.322365897664898, 'Sunkadakatte': 5.772364496368495},
'Bande Mutt': {'Kengeri': 2.354039301950788, 'Nagadevanahalli': 2.781378429591243, 'Hemmigepura': 4.094618202706603, 'Jnana Bharathi': 4.183624597563848, 'Ullalu': 4.250642960827793, 'Rajarajeshwari Nagar': 4.63816571965492, 'Malathalli': 5.0925976816055805, 'Lingadheeranahalli': 6.37617303607132, 'Srigandhadakaval': 6.680677010243954, 'Herohalli': 7.832343331802794},
'Kengeri': {'Hemmigepura': 1.7585430448268808, 'Bande Mutt': 2.354039301950788, 'Lingadheeranahalli': 4.3579001949695, 'Rajarajeshwari Nagar': 4.428681635067733, 'Nagadevanahalli': 4.805842374509415, 'Jnana Bharathi': 5.515419832922277, 'Ullalu': 6.5596400906494585, 'Malathalli': 7.108865395673957, 'Rajiv Nagar': 8.184299329473504, 'Srigandhadakaval': 8.657300560942456},
'Hemmigepura': {'Kengeri': 1.7585430448268808, 'Lingadheeranahalli': 2.9108523899771943, 'Bande Mutt': 4.094618202706603, 'Rajarajeshwari Nagar': 4.743061947463257, 'Nagadevanahalli': 6.348906127788968, 'Jnana Bharathi': 6.670280555303789, 'Rajiv Nagar': 8.172534434214715, 'Ullalu': 8.235485132329446, 'Malathalli': 8.585082750955653, 'Srigandhadakaval': 10.081295979657847},
'JP Park': {'Jalahalli': 1.3021523663915637, 'Mattikere': 1.4293538844037879, 'Yeshwanthpura': 2.0944670939213954, 'Mahalakshmipuram': 2.194562722270513, 'Radhakrishna Temple': 2.7200035804137865, 'Sanjaya Nagar': 3.042184779554178, 'Dodda Bommasandra': 3.1642897209632723, 'Subramanya Nagar': 3.20584738079129, 'Kammagondanahalli': 3.231008906552155, 'Peenya Industrial Area': 3.401782090885819},
'Yeshwanthpura': {'Laxmidevi Nagar': 1.4270211415023661, 'Peenya Industrial Area': 1.5964084558405618, 'Peenya': 1.6077110185572627, 'Laggere': 1.9114151418342389, 'JP Park': 2.0944670939213954, 'Mahalakshmipuram': 2.1784705644702282, 'Chokkasandra': 2.5517171276255843, 'Hegganahalli': 2.740849633827253, 'Rajagopal Nagar': 2.7525555458495687, 'Nagapura': 2.7890651204302928},
'Jalahalli': {'JP Park': 1.3021523663915637, 'Kammagondanahalli': 2.04348914999585, 'Mattikere': 2.205849660720794, 'Dodda Bommasandra': 2.233291010843793, 'Yeshwanthpura': 2.7955923678847867, 'Radhakrishna Temple': 3.2881543863327236, 'Sanjaya Nagar': 3.450055439397351, 'Mahalakshmipuram': 3.4830591026636144, 'T Dasarahalli': 3.555775047050571, 'Chokkasandra': 3.6048910566302275},
'Peenya': {'Peenya Industrial Area': 0.013608456520094807, 'Chokkasandra': 1.2372154422557975, 'Nalagadarenahalli': 1.3649510002944252, 'Yeshwanthpura': 1.6077110185572627, 'Laxmidevi Nagar': 1.813379769575808, 'Rajagopal Nagar': 1.9759341882741304, 'Laggere': 2.1990801940781353, 'Hegganahalli': 2.4940534356819266, 'T Dasarahalli': 2.512997844590154, 'Chowdeshwari Nagar': 2.9998277313859725},
'Laxmidevi Nagar': {'Laggere': 0.4959718901688257, 'Hegganahalli': 1.3516687824651614, 'Chowdeshwari Nagar': 1.3958717167978214, 'Yeshwanthpura': 1.4270211415023661, 'Rajagopal Nagar': 1.6380378421687323, 'Peenya Industrial Area': 1.8002473518729682, 'Peenya': 1.813379769575808, 'Nagapura': 2.3166577760543183, 'Mahalakshmipuram': 2.635068585721304, 'Shakthi Ganapathi Nagar': 2.654326464583476},
'Laggere': {'Laxmidevi Nagar': 0.4959718901688257, 'Chowdeshwari Nagar': 0.9002172624514554, 'Hegganahalli': 0.9760719257434406, 'Rajagopal Nagar': 1.5122493906955208, 'Yeshwanthpura': 1.9114151418342389, 'Peenya Industrial Area': 2.1866648350683557, 'Peenya': 2.1990801940781353, 'Nagapura': 2.2172881149031003, 'Shakthi Ganapathi Nagar': 2.317236992730096, 'Vrisabhavathi Nagar': 2.5220192737756517},
'Chowdeshwari Nagar': {'Hegganahalli': 0.8266735802932185, 'Laggere': 0.9002172624514554, 'Laxmidevi Nagar': 1.3958717167978214, 'Vrisabhavathi Nagar': 1.624579118375861, 'Rajagopal Nagar': 1.7162336439538897, 'Shakthi Ganapathi Nagar': 1.855195538812553, 'Kottegepalya': 2.2110247253182016, 'Sunkadakatte': 2.231884357468964, 'Nagapura': 2.275699855068684, 'Yeshwanthpura': 2.7953087151558043},
'Kottegepalya': {'Vrisabhavathi Nagar': 1.0051818920327944, 'Sunkadakatte': 1.0099310389547935, 'Srigandhadakaval': 1.424293204232543, 'Chowdeshwari Nagar': 2.2110247253182016, 'Hegganahalli': 2.3880938276423604, 'Herohalli': 2.4827340132140687, 'Shakthi Ganapathi Nagar': 2.8792528141747087, 'Rajagopal Nagar': 3.0061886883643174, 'Malathalli': 3.0127157762392303, 'Laggere': 3.0752139534944773},
'Srigandhadakaval': {'Kottegepalya': 1.424293204232543, 'Malathalli': 1.5895800659533779, 'Sunkadakatte': 1.9598377586973654, 'Vrisabhavathi Nagar': 2.235578336360752, 'Herohalli': 2.4163990862865594, 'Ullalu': 3.291463697130331, 'Chowdeshwari Nagar': 3.633202660895737, 'Jnana Bharathi': 3.703383187609418, 'Hegganahalli': 3.7766415608971973, 'Nagadevanahalli': 3.9076727326602274},
'Malathalli': {'Srigandhadakaval': 1.5895800659533779, 'Ullalu': 2.0639453153371727, 'Nagadevanahalli': 2.326679475702115, 'Jnana Bharathi': 2.6043528283698754, 'Kottegepalya': 3.0127157762392303, 'Herohalli': 3.267589698477601, 'Sunkadakatte': 3.4558726830191984, 'Vrisabhavathi Nagar': 3.754874380582674, 'Bande Mutt': 5.0925976816055805, 'Chowdeshwari Nagar': 5.217471731721664},
'Jnana Bharathi': {'Nagadevanahalli': 2.1038799285799508, 'Malathalli': 2.6043528283698754, 'Rajarajeshwari Nagar': 3.1836372944297078, 'Srigandhadakaval': 3.703383187609418, 'Ullalu': 3.8313108770191566, 'Bande Mutt': 4.183624597563848, 'Kottegepalya': 4.884429938775551, 'Vrisabhavathi Nagar': 5.22243221209405, 'Rajiv Nagar': 5.412625914774455, 'Kengeri': 5.515419832922277},
'Rajarajeshwari Nagar': {'Jnana Bharathi': 3.1836372944297078, 'Rajiv Nagar': 3.8044315064962886, 'Kengeri': 4.428681635067733, 'Nagadevanahalli': 4.44865850001867, 'Lingadheeranahalli': 4.516354204775913, 'Bande Mutt': 4.63816571965492, 'Hemmigepura': 4.743061947463257, 'Malathalli': 5.77050577616831, 'Ullalu': 6.60766528416646, 'Srigandhadakaval': 6.847252610467022},
'Rajiv Nagar': {'Rajarajeshwari Nagar': 3.8044315064962886, 'Shankar Matt': 4.155897660969173, 'Jnana Bharathi': 5.412625914774455, 'Lingadheeranahalli': 6.794092734077727, 'Nalvadi Krishna Raja Wadiyar': 6.816761051975978, 'Jayachamarajendra Nagar': 7.364677344821752, 'Nagadevanahalli': 7.390560527066007, 'Malathalli': 7.698920411154836, 'Srigandhadakaval': 8.090505742446561, 'Shakthi Ganapathi Nagar': 8.169092499447615},
'Mahalakshmipuram': {'Subramanya Nagar': 1.15714865071332, 'Nagapura': 1.6208414921140988, 'Gayithri Nagar': 1.7113164794778446, 'Yeshwanthpura': 2.1784705644702282, 'JP Park': 2.194562722270513, 'Malleswaram': 2.212046616778642, 'Kadu Malleshwara': 2.4610513307303186, 'Mattikere': 2.4654981210840927, 'Laxmidevi Nagar': 2.635068585721304, 'Laggere': 2.842235470089595},
'Nagapura': {'Shakthi Ganapathi Nagar': 1.2963991777929522, 'Gayithri Nagar': 1.4682807069626436, 'Subramanya Nagar': 1.5470758731355918, 'Mahalakshmipuram': 1.6208414921140988, 'Jayachamarajendra Nagar': 1.6981565723305663, 'Laggere': 2.2172881149031003, 'Chowdeshwari Nagar': 2.275699855068684, 'Laxmidevi Nagar': 2.3166577760543183, 'Malleswaram': 2.746704364880395, 'Yeshwanthpura': 2.7890651204302928},
'Nalvadi Krishna Raja Wadiyar': {'Shankar Matt': 2.887666447825473, 'Rajamahal Guttahalli': 3.3595758094851664, 'Pulikeshinagar': 3.79540146024694, 'S K Garden': 4.114047239751362, 'Kadu Malleshwara': 4.401252841039362, 'Malleswaram': 4.567961801655758, 'Devara Jeevanahalli': 4.8528525000842695, 'Sagayarapuram': 4.8729303962816255, 'Aramane Nagara': 4.9321326169265785, 'Gayithri Nagar': 4.975268960510575},
'Shankar Matt': {'Nalvadi Krishna Raja Wadiyar': 2.887666447825473, 'Rajiv Nagar': 4.155897660969173, 'Jayachamarajendra Nagar': 4.348425224331143, 'Rajamahal Guttahalli': 5.185087019059209, 'Gayithri Nagar': 5.237809170359888, 'Shakthi Ganapathi Nagar': 5.483002755545429, 'Kadu Malleshwara': 5.54646466401465, 'Malleswaram': 5.584710104621206, 'Subramanya Nagar': 5.857585763805352, 'Nagapura': 5.909336022696542},
'Shakthi Ganapathi Nagar': {'Jayachamarajendra Nagar': 1.2055210202026811, 'Nagapura': 1.2963991777929522, 'Chowdeshwari Nagar': 1.855195538812553, 'Vrisabhavathi Nagar': 1.8758049383780124, 'Laggere': 2.317236992730096, 'Gayithri Nagar': 2.4076271160967613, 'Laxmidevi Nagar': 2.654326464583476, 'Hegganahalli': 2.6815956739184514, 'Subramanya Nagar': 2.715065983672102, 'Kottegepalya': 2.8792528141747087},
'Vrisabhavathi Nagar': {'Kottegepalya': 1.0051818920327944, 'Chowdeshwari Nagar': 1.624579118375861, 'Sunkadakatte': 1.752543555750348, 'Shakthi Ganapathi Nagar': 1.8758049383780124, 'Hegganahalli': 2.1305074680644087, 'Srigandhadakaval': 2.235578336360752, 'Laggere': 2.5220192737756517, 'Jayachamarajendra Nagar': 2.8311833967696054, 'Rajagopal Nagar': 2.9500245843474704, 'Nagapura': 3.0078443599203055},
'Mattikere': {'Radhakrishna Temple': 1.2965468417495223, 'JP Park': 1.4293538844037879, 'Sanjaya Nagar': 1.6592243112953207, 'Jalahalli': 2.205849660720794, 'Mahalakshmipuram': 2.4654981210840927, 'Aramane Nagara': 3.025136772237686, 'Subramanya Nagar': 3.0477505318672504, 'Dodda Bommasandra': 3.049679960784608, 'Ganga Nagar': 3.067381296139405, 'Malleswaram': 3.140457798925695},
'Malleswaram': {'Kadu Malleshwara': 0.2622210740821591, 'Subramanya Nagar': 1.2616286098928131, 'Gayithri Nagar': 1.361926538843221, 'Rajamahal Guttahalli': 1.704860328085102, 'Aramane Nagara': 1.8846444019859525, 'Mahalakshmipuram': 2.212046616778642, 'Ganga Nagar': 2.6960436803024055, 'Nagapura': 2.746704364880395, 'Mattikere': 3.140457798925695, 'Radhakrishna Temple': 3.2053453187377965},
'Aramane Nagara': {'Ganga Nagar': 0.8452667727432303, 'Rajamahal Guttahalli': 1.60916243659794, 'Kadu Malleshwara': 1.6936692324210456, 'Malleswaram': 1.8846444019859525, 'Radhakrishna Temple': 2.309564669989575, 'Sanjaya Nagar': 2.5629819373999827, 'Chamundi Nagara': 2.5806036347889125, 'S K Garden': 2.687053724889376, 'Devara Jeevanahalli': 2.7359536209130346, 'Manorayanapalya': 2.7917473258402734},
'Rajamahal Guttahalli': {'Kadu Malleshwara': 1.45000165219892, 'Aramane Nagara': 1.60916243659794, 'Malleswaram': 1.704860328085102, 'Ganga Nagar': 2.332640580751923, 'S K Garden': 2.5247649844323905, 'Gayithri Nagar': 2.8474831037354433, 'Subramanya Nagar': 2.938215698257383, 'Devara Jeevanahalli': 2.9811136066303, 'Pulikeshinagar': 3.338581315930805, 'Nalvadi Krishna Raja Wadiyar': 3.3595758094851664},
'Kadu Malleshwara': {'Malleswaram': 0.2622210740821591, 'Rajamahal Guttahalli': 1.45000165219892, 'Subramanya Nagar': 1.5234483782102357, 'Gayithri Nagar': 1.5917066874708254, 'Aramane Nagara': 1.6936692324210456, 'Mahalakshmipuram': 2.4610513307303186, 'Ganga Nagar': 2.522631713859887, 'Nagapura': 2.998619386463364, 'Radhakrishna Temple': 3.196821047348789, 'Mattikere': 3.2367802120675666},
'Subramanya Nagar': {'Gayithri Nagar': 0.6393365099797729, 'Mahalakshmipuram': 1.15714865071332, 'Malleswaram': 1.2616286098928131, 'Kadu Malleshwara': 1.5234483782102357, 'Nagapura': 1.5470758731355918, 'Jayachamarajendra Nagar': 2.492414342864676, 'Shakthi Ganapathi Nagar': 2.715065983672102, 'Rajamahal Guttahalli': 2.938215698257383, 'Aramane Nagara': 2.9905064785755333, 'Mattikere': 3.0477505318672504},
'Gayithri Nagar': {'Subramanya Nagar': 0.6393365099797729, 'Malleswaram': 1.361926538843221, 'Nagapura': 1.4682807069626436, 'Kadu Malleshwara': 1.5917066874708254, 'Mahalakshmipuram': 1.7113164794778446, 'Jayachamarajendra Nagar': 1.9567394481089162, 'Shakthi Ganapathi Nagar': 2.4076271160967613, 'Rajamahal Guttahalli': 2.8474831037354433, 'Aramane Nagara': 3.2366200064290496, 'Laggere': 3.638826783550392},
'Radhakrishna Temple': {'Sanjaya Nagar': 0.4814723544440649, 'Mattikere': 1.2965468417495223, 'Ganga Nagar': 2.0424827778347097, 'Aramane Nagara': 2.309564669989575, 'Hebbala': 2.5159344126553695, 'Chamundi Nagara': 2.638684338296157, 'JP Park': 2.7200035804137865, 'Manorayanapalya': 3.1086874154674224, 'Vishwanath Nagenahalli': 3.1290299515330733, 'Kadu Malleshwara': 3.196821047348789},
'Sanjaya Nagar': {'Radhakrishna Temple': 0.4814723544440649, 'Mattikere': 1.6592243112953207, 'Ganga Nagar': 2.1431372292198416, 'Hebbala': 2.2039557698376266, 'Chamundi Nagara': 2.390344784825104, 'Aramane Nagara': 2.5629819373999827, 'Vishwanath Nagenahalli': 2.7725817510637834, 'Manorayanapalya': 2.874342728983857, 'Byatarayanapura Ward': 2.919608301633805, 'JP Park': 3.042184779554178},
'Hebbala': {'Chamundi Nagara': 0.4252075421287434, 'Vishwanath Nagenahalli': 0.6820884001261157, 'Manorayanapalya': 0.8199282730414067, 'Kaval Bairasandra': 1.6450525788841033, 'Nagavara': 1.7686055037901565, 'Hebbal Kempapura Ward': 1.9633735380319635, 'Ganga Nagar': 1.9818671618363461, 'Sanjaya Nagar': 2.2039557698376266, 'Radhakrishna Temple': 2.5159344126553695, 'Kushal Nagar': 2.6304943937512797},
'Vishwanath Nagenahalli': {'Hebbala': 0.6820884001261157, 'Chamundi Nagara': 0.9032268702103449, 'Manorayanapalya': 0.9616596433898413, 'Nagavara': 1.0997889492819721, 'Hebbal Kempapura Ward': 1.5879139164787193, 'Kaval Bairasandra': 1.738917750588882, 'Kushal Nagar': 2.5369477227274984, 'Ganga Nagar': 2.622678614277045, 'HBR Layout': 2.679947200267947, 'Kadugondanahalli': 2.7490501999978854},
'Manorayanapalya': {'Chamundi Nagara': 0.48715920795357354, 'Hebbala': 0.8199282730414067, 'Kaval Bairasandra': 0.8378898803333162, 'Vishwanath Nagenahalli': 0.9616596433898413, 'Nagavara': 1.6777979275724468, 'Kushal Nagar': 1.8140176805266075, 'Ganga Nagar': 1.978008269332604, 'Kadugondanahalli': 2.0354314655907966, 'Devara Jeevanahalli': 2.177675579332007, 'Hebbal Kempapura Ward': 2.5412698508626703},
'Chamundi Nagara': {'Hebbala': 0.4252075421287434, 'Manorayanapalya': 0.48715920795357354, 'Vishwanath Nagenahalli': 0.9032268702103449, 'Kaval Bairasandra': 1.2566272653838129, 'Ganga Nagar': 1.7380498166370528, 'Nagavara': 1.876513682082335, 'Kushal Nagar': 2.2826371429783316, 'Hebbal Kempapura Ward': 2.3551703876397805, 'Sanjaya Nagar': 2.390344784825104, 'Devara Jeevanahalli': 2.490345910290496},
'Ganga Nagar': {'Aramane Nagara': 0.8452667727432303, 'Chamundi Nagara': 1.7380498166370528, 'Manorayanapalya': 1.978008269332604, 'Hebbala': 1.9818671618363461, 'Radhakrishna Temple': 2.0424827778347097, 'Kaval Bairasandra': 2.113626839970768, 'Sanjaya Nagar': 2.1431372292198416, 'Rajamahal Guttahalli': 2.332640580751923, 'Devara Jeevanahalli': 2.419711235308525, 'Kadu Malleshwara': 2.522631713859887},
'Jayachamarajendra Nagar': {'Shakthi Ganapathi Nagar': 1.2055210202026811, 'Nagapura': 1.6981565723305663, 'Gayithri Nagar': 1.9567394481089162, 'Subramanya Nagar': 2.492414342864676, 'Vrisabhavathi Nagar': 2.8311833967696054, 'Chowdeshwari Nagar': 3.059007230043487, 'Mahalakshmipuram': 3.1477539398133216, 'Malleswaram': 3.2134842035803173, 'Kadu Malleshwara': 3.392086390799654, 'Laggere': 3.4452844539085796},
'Kaval Bairasandra': {'Manorayanapalya': 0.8378898803333162, 'Kushal Nagar': 1.0707830270560363, 'Chamundi Nagara': 1.2566272653838129, 'Kadugondanahalli': 1.285448093342049, 'Devara Jeevanahalli': 1.3942282535860913, 'Hebbala': 1.6450525788841033, 'Vishwanath Nagenahalli': 1.738917750588882, 'Sagayarapuram': 2.0893554235643235, 'S K Garden': 2.0933024414774213, 'Ganga Nagar': 2.113626839970768},
'Kushal Nagar': {'Kadugondanahalli': 0.22141818689962858, 'Kaval Bairasandra': 1.0707830270560363, 'Lingarajapura': 1.2401779565475832, 'Devara Jeevanahalli': 1.312292151018034, 'Sagayarapuram': 1.4236545501084614, 'Kacharkanahalli': 1.686669976765324, 'Manorayanapalya': 1.8140176805266075, 'S K Garden': 2.01487811066262, 'HBR Layout': 2.105819171739814, 'Chamundi Nagara': 2.2826371429783316},
'Muneshwara Nagar': {'Begur': 2.1994096477435723, 'Rajiv Nagar': 9.852131605036112, 'Nalvadi Krishna Raja Wadiyar': 10.00781116069569, 'Shankar Matt': 10.233371566171927, 'Pulikeshinagar': 11.67033547364202, 'Sagayarapuram': 12.71668667412085, 'S K Garden': 12.770082051702353, 'Banasavadi': 12.79821557383081, 'Subbayyanapalya': 13.05960633951234, 'Lingarajapura': 13.2066083394056},
'Devara Jeevanahalli': {'S K Garden': 0.740047095452962, 'Sagayarapuram': 0.9910156488050668, 'Kushal Nagar': 1.312292151018034, 'Kadugondanahalli': 1.3446294399211334, 'Kaval Bairasandra': 1.3942282535860913, 'Pulikeshinagar': 1.7066815910159214, 'Lingarajapura': 1.8797120891031471, 'Manorayanapalya': 2.177675579332007, 'Ganga Nagar': 2.419711235308525, 'Chamundi Nagara': 2.490345910290496},
'S K Garden': {'Devara Jeevanahalli': 0.740047095452962, 'Sagayarapuram': 1.154131035610493, 'Pulikeshinagar': 1.2377036361648284, 'Kadugondanahalli': 2.009438985353466, 'Kushal Nagar': 2.01487811066262, 'Kaval Bairasandra': 2.0933024414774213, 'Lingarajapura': 2.302772996026484, 'Rajamahal Guttahalli': 2.5247649844323905, 'Ganga Nagar': 2.602606021329472, 'Aramane Nagara': 2.687053724889376},
'Sagayarapuram': {'Devara Jeevanahalli': 0.9910156488050668, 'S K Garden': 1.154131035610493, 'Pulikeshinagar': 1.175530106515131, 'Lingarajapura': 1.1913883799320601, 'Kadugondanahalli': 1.2971494971974993, 'Kushal Nagar': 1.4236545501084614, 'Kacharkanahalli': 1.877382771386809, 'Kaval Bairasandra': 2.0893554235643235, 'Kammanahalli': 2.4509114461579142, 'Manorayanapalya': 2.926756034687795},
'Pulikeshinagar': {'Sagayarapuram': 1.175530106515131, 'S K Garden': 1.2377036361648284, 'Devara Jeevanahalli': 1.7066815910159214, 'Lingarajapura': 2.2077661999287566, 'Kadugondanahalli': 2.46947622473166, 'Kushal Nagar': 2.581311489439776, 'Kacharkanahalli': 2.822851821573912, 'Kaval Bairasandra': 3.0688111845669837, 'Kammanahalli': 3.2950728448092574, 'Rajamahal Guttahalli': 3.338581315930805},
'Hennur': {'HBR Layout': 1.6247489942686477, 'Kammanahalli': 2.3648171069193102, 'Thanisandra Ward': 2.4799048791399105, 'Kacharkanahalli': 2.6208896178436567, 'Subbayyanapalya': 2.6436849691769497, 'Banasavadi': 2.9465964212700237, 'Lingarajapura': 3.1950416101853873, 'Nagavara': 3.292502358414408, 'Kadugondanahalli': 3.3291273620842503, 'Kushal Nagar': 3.3929929479068175},
'Nagavara': {'Vishwanath Nagenahalli': 1.0997889492819721, 'Manorayanapalya': 1.6777979275724468, 'Hebbala': 1.7686055037901565, 'Hebbal Kempapura Ward': 1.7807075225521938, 'HBR Layout': 1.7822961939481399, 'Chamundi Nagara': 1.876513682082335, 'Kaval Bairasandra': 2.1350035799240015, 'Kushal Nagar': 2.4959488739215074, 'Thanisandra Ward': 2.5675578650272883, 'Kadugondanahalli': 2.6631310278662843},
'HBR Layout': {'Hennur': 1.6247489942686477, 'Nagavara': 1.7822961939481399, 'Kushal Nagar': 2.105819171739814, 'Kadugondanahalli': 2.1282041569183545, 'Kacharkanahalli': 2.215785233507377, 'Thanisandra Ward': 2.349738039885597, 'Kammanahalli': 2.382451319026926, 'Lingarajapura': 2.47422784746688, 'Kaval Bairasandra': 2.564596436365597, 'Vishwanath Nagenahalli': 2.679947200267947},
'Kadugondanahalli': {'Kushal Nagar': 0.22141818689962858, 'Lingarajapura': 1.0188163851066299, 'Kaval Bairasandra': 1.285448093342049, 'Sagayarapuram': 1.2971494971974993, 'Devara Jeevanahalli': 1.3446294399211334, 'Kacharkanahalli': 1.484188983829211, 'S K Garden': 2.009438985353466, 'Manorayanapalya': 2.0354314655907966, 'Kammanahalli': 2.097279136998644, 'HBR Layout': 2.1282041569183545},
'Kacharkanahalli': {'Kammanahalli': 0.6292037861925269, 'Lingarajapura': 0.693164875024527, 'Kadugondanahalli': 1.484188983829211, 'Subbayyanapalya': 1.5198167337453548, 'Kushal Nagar': 1.686669976765324, 'Banasavadi': 1.834673391132812, 'Sagayarapuram': 1.877382771386809, 'HBR Layout': 2.215785233507377, 'Devara Jeevanahalli': 2.5501470649060374, 'Hennur': 2.6208896178436567},
'Kammanahalli': {'Kacharkanahalli': 0.6292037861925269, 'Subbayyanapalya': 0.9242636613871409, 'Banasavadi': 1.268520034077541, 'Lingarajapura': 1.2994010178409479, 'Kadugondanahalli': 2.097279136998644, 'Kushal Nagar': 2.2914617663254684, 'Hennur': 2.3648171069193102, 'HBR Layout': 2.382451319026926, 'Sagayarapuram': 2.4509114461579142, 'Devara Jeevanahalli': 3.1733647345700273},
'Banasavadi': {'Subbayyanapalya': 0.3698774618113107, 'Kammanahalli': 1.268520034077541, 'Kacharkanahalli': 1.834673391132812, 'Lingarajapura': 2.3914147265365635, 'Hennur': 2.9465964212700237, 'Kadugondanahalli': 3.314815950688115, 'Sagayarapuram': 3.375793299219827, 'HBR Layout': 3.492097923548544, 'Kushal Nagar': 3.52054257396552, 'Pulikeshinagar': 3.9302525161079958},
'Subbayyanapalya': {'Banasavadi': 0.3698774618113107, 'Kammanahalli': 0.9242636613871409, 'Kacharkanahalli': 1.5198167337453548, 'Lingarajapura': 2.120461956980959, 'Hennur': 2.6436849691769497, 'Kadugondanahalli': 3.003897508939983, 'HBR Layout': 3.1239872093986203, 'Sagayarapuram': 3.1689639243447316, 'Kushal Nagar': 3.204320941841168, 'Pulikeshinagar': 3.8178263943109294},
'Lingarajapura': {'Kacharkanahalli': 0.693164875024527, 'Kadugondanahalli': 1.0188163851066299, 'Sagayarapuram': 1.1913883799320601, 'Kushal Nagar': 1.2401779565475832, 'Kammanahalli': 1.2994010178409479, 'Devara Jeevanahalli': 1.8797120891031471, 'Subbayyanapalya': 2.120461956980959, 'Pulikeshinagar': 2.2077661999287566, 'Kaval Bairasandra': 2.2928405877219378, 'S K Garden': 2.302772996026484},
'Begur': {'Muneshwara Nagar': 2.1994096477435723, 'Rajiv Nagar': 10.207537957669707, 'Shankar Matt': 11.395917604908925, 'Nalvadi Krishna Raja Wadiyar': 11.623807360105971, 'Lingadheeranahalli': 13.3710066027624, 'Rajarajeshwari Nagar': 13.37113720997208, 'Pulikeshinagar': 13.641054256801892, 'S K Garden': 14.693364813532895, 'Sagayarapuram': 14.722997019241559, 'Rajamahal Guttahalli': 14.94134253104923},
}



# A* search functions
class Node:
    def __init__(self, ward, g_cost, h_cost, parent=None):
        self.ward = ward
        self.g_cost = g_cost
        self.h_cost = h_cost
        self.parent = parent

    def f_cost(self):
        return self.g_cost + self.h_cost

def a_star(start, end, wards):
    # A* algorithm implementation
    open_list = []
    closed_set = set()

    start_node = Node(start, 0, calculate_heuristic(start, end))
    end_node = Node(end, 0, 0)

    heapq.heappush(open_list, (start_node.f_cost(), start_node))

    while open_list:
        current = heapq.heappop(open_list)[1]
        closed_set.add(current.ward)

        if current.ward == end_node.ward:
            return reconstruct_path(current), current.g_cost
        if current.ward in distances:
            for neighbor_ward in distances[current.ward]:
                if neighbor_ward in closed_set:
                    continue

                g_cost = current.g_cost + distances[current.ward][neighbor_ward]
                h_cost = calculate_heuristic(neighbor_ward, end)

                neighbor_node = Node(neighbor_ward, g_cost, h_cost, parent=current)
                heapq.heappush(open_list, (neighbor_node.f_cost(), neighbor_node))

    return None, 0

def euclidean_distance(a, b):
    x1, y1 = a
    x2, y2 = b
    return math.hypot(x2 - x1, y2 - y1)

def manhattan_distance(a, b):
    x1, y1 = a
    x2, y2 = b
    return abs(x2 - x1) + abs(y2 - y1)

def calculate_heuristic(from_ward, to_ward):
    # Heuristic calculation
    euclidean_dist = 0.2 * euclidean_distance(wards[from_ward], wards[to_ward])
    manhattan_dist = 0.8 * manhattan_distance(wards[from_ward], wards[to_ward])
    traffic_density = get_traffic_density(from_ward, to_ward)

    # Get predicted travel times from PredictTime.py
    predicted_times = get_predicted_times(from_ward, to_ward)
    travel_time_factor = 0.5 * (predicted_times[0] + predicted_times[1])  # Average of both travel times

    return euclidean_dist + manhattan_dist + travel_time_factor + traffic_density

def reconstruct_path(current_node):
    # Path reconstruction
    path = [current_node.ward]
    while current_node.parent:
        current_node = current_node.parent
        path.insert(0, current_node.ward)
    return path

def calculate_total_time(path, start, end):
    total_time = 0
    for i in range(len(path) - 1):
        from_ward = path[i]
        to_ward = path[i + 1]
        predicted_times = get_predicted_times(from_ward, to_ward)
        total_time += sum(predicted_times)  # Add both predicted times
    return total_time


# Main program
start = input("Enter your Start ward:")
end = input("Enter your destination ward:")

result, total_distance = a_star(start, end, wards)

if result:
    total_time = calculate_total_time(result, start, end)
    print("Shortest path from", start, "to", end, ":", " -> ".join(result))
    print(f"Total distance: {total_distance:.2f} km")
    print(f"Total time: {total_time/60:.2f} minutes")

    # Map generation and printing
    my_map = folium.Map(location=[12.9716, 77.5946], zoom_start=11)

    # Add markers for all nodes (blue)
    for ward, coords in wards.items():
        folium.Marker(coords, tooltip=ward, icon=folium.Icon(color='blue')).add_to(my_map)

    # Mark the start and end nodes (red)
    folium.Marker(wards[start], tooltip=start, icon=folium.Icon(color='red')).add_to(my_map)
    folium.Marker(wards[end], tooltip=end, icon=folium.Icon(color='red')).add_to(my_map)

    # Mark the path nodes (red)
    for ward in result:
        folium.Marker(wards[ward], tooltip=ward, icon=folium.Icon(color='red')).add_to(my_map)

    # Draw the path with blue lines
    path_coords = [wards[ward] for ward in result]
    folium.PolyLine(locations=path_coords, color='blue', weight=5, opacity=0.8).add_to(my_map)

    # Save the map as an HTML file
    my_map.save('map.html')

    # Open the map in the default web browser
    import webbrowser
    webbrowser.open('map.html')
else:
    print("No path found between", start, "and", end)