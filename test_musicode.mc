hands_declaration{ #nombre de mains limité à 4
	
	main Md1 = MD_Alex
	main Mg1 = MD_Yvan  

	main Md1 = MG_Elias  
	main Md2 = None}

play{

	mesure = 0;
	nbr_mesure;
	while (mesure < nbr_mesure, mesure inc){

		intens intensity = 3
		acc accord = \do,ré,mi/
		
		notes notesMd1 = [do,ré,mi,fa]
		notes notesMg1 = [do2,ré2,mi2,accord]

		play(Md1,notes[mesure%4],intensity)
		play(Mg1,notes[mesure%4],intensity)

		Melody(Md1,intensity)

	}
}

def Melody(Md1,intensity){

	Md1.play(do,intensity)

}
