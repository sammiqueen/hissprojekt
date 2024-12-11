# Hissprojekt - Post Mortem
Samantha Ågren
2024-12-11
## Inledning
Målet med projektet var att under en period på cirka 2 månader skriva ett script i Programmeringsspråket Python med syfte att på ett trovärdigt sätt uppvisa hur en hissalgoritm skulle kunna se ut. Projektet genomfördes ensam genom programmering i Visual Studio Code, en IDE utvecklad av Microsoft. Genom projektet har målet med arbetet förändrats, från att inledningsvis inkludera en version av algoritmen konstruerad med Redstone-komponenter i spelet Minecraft till en version där detta omitterades till förmån för en snävare tidsplan.
## Bakgrund
Hissprojektet inleddes med ett studiebesök på en hissanläggning i centrala Umeå. Till detta stadie valdes hissen i läraringången på NTI Gymnasiet Umeå. Hissen som undersöktes hade 4 våningar, och ett test genomfördes för att undersöka hur hissen prioriterade olika våningar vid olika knapptryck. En algoritmbeskrivning nedtecknades över hur hissens grundläggande våningsväljarmetod fungerade. Denna algoritmbeskrivning användes sedan som grund i programmeringsstadiet av projektet

Programmeringsstadiet inleddes med att ett flödeschema konstruerades, vilket på ett mer lättöverskådligt sätt beskrev hissens våningsväljande process. Efter ett initialt bakslag där en onödigt komplicerad metod användes för att beskriva algoritmen skrevs sedan den grundläggande metoden för hissens algoritm. Metoden fungerar genom att hela tiden ha en lista på nästföljande våningar hissen ska besöka, och genom att sortera den listan bestämmer algoritmen vilken våning hissen ska besöka härnäst.