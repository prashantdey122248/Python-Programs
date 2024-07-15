// // let decompressed = (str) => {
// //     let decompressedString = '';

// //     for (let i = 0; i < str.length; i++) {
// //         let mul = '';
// //         let char = str[i];

// //         while (!isNaN(parseInt(str[i + 1]))) {
// //             mul += str[i + 1];
// //             i++;
// //         }

// //         mul = parseInt(mul) || 1;
// //         console.log(char);
// //         console.log(mul);

// //         decompressedString += char.repeat(mul);
// //     }

// //     return decompressedString;
// // }


// // console.log(decompressed('A5T2C3G4A2'));

// const new_fun = (string) => {
//     let str = ''
//     let split_obj = {}
//     for (let i = 0; i < string.length; i + 2) {
//         const element = string[i];
//         // 'A5 T2 C3 G4 A2 T'
//         let ch = '';
//         let num = 0;
//         if (isNaN(element)) {
//             ch = element;
//         }
//         else if (element) {
//             num = element;
//         }
//         else {
//             num = 1
//         }
//         str += ch.repeat(num);
//     }

//     console.log(str)
// }

// new_fun('A5T2C3G4A2T')
// let decompressed = (str) => {
//     let decompressedString = '';

//     for (let i = 0; i < str.length; i++) {
//         let mul = '';
//         let char = str[i];

//         while (!isNaN(parseInt(str[i + 1]))) {
//             mul += str[i + 1];
//             i++;
//         }

//         mul = parseInt(mul) || 1;
//         console.log(char);
//         console.log(mul);

//         decompressedString += char.repeat(mul);
//     }

//     return decompressedString;
// }


// console.log(decompressed('A5T2C3G4A2'));
const new_fun = (string) => {
    let decompressedString = '';

    for (let i = 0; i < string.length; i++) {
        let ch = string[i];
        let num = '';

        // Collect digits to form the number
        while (!isNaN(parseInt(string[i + 1]))) {
            num += string[i + 1];
            console.log(num)
            i++;
        }

        // Convert num to integer or default to 1 if num is empty
        num = parseInt(num) || 1;

        // Append characters to the decompressed string
        decompressedString += ch.repeat(num);
    }

    console.log(decompressedString);
}

new_fun('A5T2C3G4A2T');