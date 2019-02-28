##### main system for shaolin airlines!!

buyTix()
{
}

checkTix()
{
}

#home interface
echo "Welcome to Shaolin Airlines, The Best Way to Fly!"
sleep(1)
echo "[1] Buy tickets"
echo "[2] Check Status"

while : #while loop to ensure correct opt is chosen
	read -p "Choose option: " option
	if [[ $option == '1' ]] #buying tickets
	then
		buyTix
	elif [[ $option == '2' ]] #checking status
	then
		checkTix
	else
		echo "Error: Not an option. Try again."
