const player = {
    name: 'chaehoon',
    points: 10,
    fat: true,
};

console.log(player);
console.log(player.name);
console.log(player['name']);

player.fat = false;
console.log(player);

player.lastName = 'Gwak';
console.log(player);
