#!/bin/bash

function press_enter {
	printf "\n"
	printf "Press Enter to continue..."
	read
	clear
}

selection=
until [ "$selection" = "0" ]; do
	printf "\nSelect from the menu: \n\n" 
	printf "  1) VM Connection Test\n"
	printf "  2) List all Containers\n"
	printf "  3) List Running Containers\n"
	printf "  4) Inspect a Container\n"
	printf "  5) Delete a Container\n"
	printf "  6) Delete all Containers\n"
	printf "  7) Create a Container from an Image\n"
	printf "  8) Restart a Container\n"
	printf "  9) Stop a Container\n"
	printf " 10) Show Logs from a Container\n"
	printf " 11) List all Images\n"
	printf " 12) Delete an Image\n"
	printf " 13) Delete all Images\n"
	printf " 14) TAG an Image\n"
	printf " 15) Create Docker Images from Local Dockerfile\n"
	printf " \n 16) Exit\n"

	printf "Selection: "
	read selection

	case $selection in
		1  ) 	telnet snf-35297.vm.okeanos-global.grnet.gr 8083 
			press_enter
			;;
		2  )   	curl -s -X GET -H 'Accept: application/json' http://83.212.127.216:8083/containers | python -mjson.tool
			press_enter
			;;
		3  ) 	curl -s -X GET -H 'Accept: application/json' http://83.212.127.216:8083/containers?state=running | python -mjson.tool
			press_enter
			;;
		4  ) 	curl -s -X GET -H 'Accept: application/json' http://83.212.127.216:8083/containers/5e2279d896de | python -mjson.tool
			press_enter
			;;
		5  ) 	curl -s -X DELETE -H 'Accept: application/json' http://83.212.127.216:8083/containers/5e2279d896de | python -mjson.tool
			press_enter
			;;
		6  ) 	curl -s -X DELETE -H 'Accept: application/json' http://83.212.127.216:8083/containersDel | python -mjson.tool
			press_enter
			;;
		7  ) 	curl -X POST -H 'Content-Type: application/json' http://83.212.127.216:8083/containers -d '{"image": "fb434121fc77"}' | python -mjson.tool
			press_enter
			;;
		8  )	curl -X PATCH -H 'Content-Type: application/json' http://83.212.127.216:8083/containers/5e2279d896de -d '{"state": "running"}'
			press_enter
			;;
		9  ) 	curl -X PATCH -H 'Content-Type: application/json' http://83.212.127.216:8083/containers/5e2279d896de -d '{"state": "stopped"}'
			press_enter
			;;
		10 )	curl -s -X GET -H 'Accept: application/json' http://83.212.127.216:8083/containers/5e2279d896de/logs | python -mjson.tool 
			press_enter
			;;
		11 )	curl -s -X GET -H 'Accept: application/json' http://83.212.127.216:8083/images | python -mjson.tool
			press_enter
			;;
		12 )	curl -s -X DELETE -H 'Accept: application/json' http://83.212.127.216:8083/images/imgID | python -mjson.tool
			press_enter
			;;
		13 )	curl -s -X DELETE -H 'Accept: application/json' http://83.212.127.216:8083/containersDel | python -mjson.tool
			press_enter
			;;
		14 )	curl -s -X PATCH -H 'Content-Type: application/json' http://83.212.127.216:8083/images/fb434121fc77 -d '{"tag": "test:1.0"}'
			press_enter
			;;
		15 )	curl -H 'Accept: application/json' -f file=@Dockerfile http://83.212.127.216:8083/images | python -mjson.tool
			press_enter
			;;
		16) exit
			;;
		* ) printf "You did not choose a valid option!\n"
	esac
done

printf "\n"
