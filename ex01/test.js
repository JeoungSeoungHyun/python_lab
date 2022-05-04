list1 = [1,2,3];
[123]
console.log(list1);

// 스프레드(...)
list1 = [...list1,4]

console.log(list1);

let user = {
    id:1,
    username:"cos"
}

// 스프레드에 같은 키 값이 있으면 업데이트한다.
user = {...user,username:"ssar"}

console.log(user);
