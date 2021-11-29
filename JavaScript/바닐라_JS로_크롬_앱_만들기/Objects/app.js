const player = {
    name: 'chaehoon',
    points: 10,
    fat: true,
};

// 오브젝트 출력
console.log(player);

// 오브젝트 원소 출력
console.log(player.name);
console.log(player['name']);

// 기존의 값 update
player.fat = false;
console.log(player);

// 새로운 값 추가
player.lastName = 'Gwak';
console.log(player);
