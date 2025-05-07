const fs = require('fs');

for (let i = 1; i <= 9; i++) {
    fs.writeFile(`guia-4/cadenas/ejercicio_${i}.py`, "", (err) => {
        if (err) {
          console.error('Error al crear el archivo:', err);
        } else {
          console.log('Archivo creado y contenido escrito correctamente.');
        }
      });
}