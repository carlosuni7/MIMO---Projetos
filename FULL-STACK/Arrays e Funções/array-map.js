
        // array de medida de temperatura
        const fahrenheit = [72, 68, 70, 70, 74, 77, 75, 79];
        console.log(fahrenheit)
        const celsius = [];

        // Usamos o for (elemet) para percorrer o array e definir uma execução
        // pra cada vez que ele passar por um indice do array
        for (const element of fahrenheit){
            let c = (element - 32) * (5 / 9);
            celsius.push(c.toFixed(2));
        }
        console.log(celsius)

        const values = [56, 27, 19, 20, 38];


        // const queue = ["Sarah", "Hank", "Anna", "Beatrice"];

        // const displayQueue = queue.map(
        //     function (element, index) {
        //         return `${index}: ${element}`;
        //     });
        // console.log(displayQueue);

