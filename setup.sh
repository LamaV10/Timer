echo "What do you want to modify?"
echo "Wich Song is going to be played (1) or path of the Timer-folder in timer.sh (2):"
read modify



echo "Which editor do you want to use?"
echo "1: NeoVim"
echo "2: Vim"
echo "3: Nano"
echo "4: Vscodium"
echo "5: Vscode"
echo "Your editors number: "

read ide

  if [ $ide -eq 1 ]; then
    ide=nvim

  elif [ $ide -eq 2 ]; then
    ide=vim

  elif [ $ide -eq 3 ]; then
    ide=nano
  
  elif [ $ide -eq 4 ]; then
    ide=vscodium
  
  elif [ $ide -eq 5 ]; then
    ide=code

  elif [ $ide -ne "12345" ]; then
    echo "Invalid number for editor!"

fi


if [ $modify -eq 1 ]; then
  cd Source/
  $ide music.py
fi

if [ $modify -eq 2 ]; then
  $ide timer.sh 
fi 
