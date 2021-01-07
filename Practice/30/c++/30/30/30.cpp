#include<iostream>

#include<vector>

#include<ctime>

using namespace std;




struct Item
{
	enum class ItemType
	{
		COIN,
		RUNE,
		WEAPON,
		ARMOR
	};

	union 
	{
		Coin coin;
		Rune rune;
		Weapon weapon;
		Armor armor;
	};

};



vector<Item> LootBox;



struct Coin 
{
	unsigned int count;
};

struct Rune 
{
	short level;
	enum class Elenemt 
	{
		FIRE,
		WATER,
		EARTH,
		AIR
	};
};

struct Weapon 
{
	unsigned int damage;
	short critical;
	short durability;
};

struct Armor 
{
	unsigned int guard;
	short durability;
};

int main()
{

	


}


