// #[derive(Debug)] // #[...] is an attribute on Direction. derive(Debug) asks the compiler to auto-generate a suitable implementation of the Debug trait
// enum Direction {
// 	up,
// 	down,
// 	left,
// 	right
// }

// #[derive(Debug)]
// struct Name {
// 	field: Type
// } // ex. in main let x = Name {field: Value};

// struct Name(Type1, Type2, Type3); // Tuple struct. in main let x = Name(Value1, Value2, Value3); then use dot notation to access

// const CONST: Type = init;

// fn name(arg: Type) -> RetType { // function syntax
// 	unimplemented!();
// }

#[derive(Debug)]
struct Cat<'a> { // need to declare lifetime 'a
	name: &'a str,
	color: &'a str,
	age: u8
}

fn print_cat(cat: &Cat) {
	println!("My cat's name is {}, color is {}, and age {}.", cat.name, cat.color, cat.age);
}

fn main() {
    println!("Hello, world!");
    println!("my first application lmao");
    let mut x = 5;
    /* immutables are like const in c++
    except constants have to be defined right then and there.
	Immutable variables don't. And constants declared in the global scope.
	A variable is immutable by default unless you put mut keyword.
    */
    // let y: u32 = 2; // specify data type syntax
    // println!("{} {}", x, y);
    // if-else statments are the same like in c
    loop {  // inf loop
    	x += 1;
    	if x < 10 {
    		continue;
    	} else if x > 10{
    		break;
    	} else {
    		println!("x is: {}", x);
    	}
    }
    println!("x now is: {}", x);
    // let num = 10..20; // range from 10 to 20
    let food = vec!["chicken", "tofu", "beef", "parfait"]; // vector
    for (i,x) in food.iter().enumerate() { // need iter() otherwise can't access vector outside of loop
    	println!("I like would like to eat: {} {}", i, x);	
    }
    // enum ex ============================================
    // let player_facing: Direction = Direction::down;

    // match player_facing { // match is like a switch statement
    // 	Direction::up => println!("player is facing up"),
    // 	Direction::down => println!("player is facing down"),
    // 	Direction::left => println!("player is facing left"),
    // 	Direction::right => println!("player is facing right"),
    // }
    // enum ex =============================================

    // tuple ex ============================================
    let morefood = (1, 2.3, "cheese", "potato", ("eggs", "yogurt", "milk"));
    println!("I want: {}", (morefood.4).1);
    // tuple ex ============================================

    {
    	/*
    	A code block: has access to things outside it's scope while the outside has no access inside.
    	*/
    }
    // pass by reference ======================================
    let my_cat = Cat{name: "Charlie", color: "milk", age: 3};
    print_cat(&my_cat); // Note: if we do not pass by ref then the value of my_cat has moved and is no longer in this scope.

}
