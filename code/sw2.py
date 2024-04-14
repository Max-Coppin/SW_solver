# Importation des modules contenant les sous-routines
import sw2fcom
import swfft
import swinit
import swstep

# Lecture des arguments de la ligne de commande
fnm = sw2fcom.get_arg(1)
fnm1 = sw2fcom.get_arg(2)

# Appel des sous-routines
# Vous devez appeler les sous-routines dans l'ordre approprié ici
# Par exemple :
swinit.swinit()
swstep.swstep()
