#include <SFML/Graphics.hpp>
#include <iostream>
// Library effective with Linux
#include <unistd.h>
#include <cstring>
using namespace sf;
 int map[5][5] = {
    1,1,1,1,1,
    1,2,1,2,1,
    1,0,1,0,1,
    1,0,0,0,1,
    1,0,0,0,1
    };
sf::RectangleShape rectangles[5];
	
Texture texture;
Texture tex_soldier;
	
int player_x = 2;
int player_y = 4;
bool is_visible = false;
struct Enemy{
private:
        int health = 100;        
public:
        int getHP(){
                return health;
        }
        void setHP(int hp){
                health += hp;
        }     
};

void rendering(RectangleShape rects[], int columns[], int tex_nums[]){
         if (!texture.loadFromFile("brick_wall.jpg"))
    {
       // error...
       std::cout<<"brick_wall.jpg not found!"<<std::endl;
    }
     if (!tex_soldier.loadFromFile("soldier.png"))
    {
       // error...
       std::cout<<"soldier.png not found!"<<std::endl;
    }
        for(int i = 0; i < 3; i++){
        //rects[i].setFillColor(sf::Color::Green);
        float h = 480.f;
        float c {h / columns[i]+1};        // c = 5.2
        if(tex_nums[i]==1){
                rects[i].setTexture(&tex_soldier);
        }
        else{
                rects[i].setTexture(&texture);
        }
        rects[i].setSize(sf::Vector2f(210,c));
        rects[i].setPosition(sf::Vector2f(i*210, 240-c/2));
    }
}
void raycasting(int x, int y, Enemy enemy) {
        
    static int tmp[3] = {0, 0, 0};
    static int tex_nums[3] = {0,0,0};
    // Обнуление временного массива перед новым вычислением
    std::fill(tmp, tmp + 3, 0);
    std::fill(tex_nums, tex_nums + 3, 0);

    for (int i = y; i >= 0; i--) {
        // Проверяем на границы
        if (x - 1 >= 0 && map[i][x - 1] == 0) tmp[0]++;
        
        
        if (map[i][x] == 0) tmp[1]++;
        if (x + 1 < 5 && map[i][x + 1] == 0) tmp[2]++;
       
         
        if (map[i][x] == 2 && enemy.getHP()>0){ tex_nums[1] = 1; is_visible = true;}
              
    }
    if(tmp[0] == 0) tmp[0] = 1;
    if(tmp[2] == 0) tmp[2] = 1;
    std::cout << x << " " << y << std::endl;
    std::cout << tmp[0] << " " << tmp[1] << " " << tmp[2] << std::endl;
    rendering(rectangles, tmp, tex_nums);
}

int main()
{
    sf::RenderWindow window(sf::VideoMode(630, 480), "SFML works!");
   
    Enemy soldier;

    raycasting(player_x, player_y,soldier);
    while (window.isOpen())
    {
        sf::Event event;
        while (window.pollEvent(event))
        {
            if (event.type == sf::Event::Closed)
                window.close();              
        }    
	if (sf::Keyboard::isKeyPressed(sf::Keyboard::Up))
        {
                player_y-=1;
                sleep(1);               
                raycasting(player_x, player_y, soldier);               
        }
        if (sf::Keyboard::isKeyPressed(sf::Keyboard::Down))
        {
                player_y+=1;
                  sleep(1); 
                raycasting(player_x, player_y, soldier);        
        }

        if (sf::Keyboard::isKeyPressed(sf::Keyboard::Left))
        {  
               player_x -=1;
                sleep(1);
                raycasting(player_x, player_y, soldier);             
        }
        if (sf::Keyboard::isKeyPressed(sf::Keyboard::Right))
        {
                player_x +=1;
                sleep(1);
                raycasting(player_x, player_y, soldier);              
        }
        if (sf::Keyboard::isKeyPressed(sf::Keyboard::Space))
        {
                if(is_visible ==true){
                        std::cout<<"Fire!"<<std::endl;
                        soldier.setHP(-50);
                         std::cout<<soldier.getHP()<<std::endl;
                };
                 sleep(1);
                 raycasting(player_x, player_y, soldier);         
        }      
        window.clear();
        for(int i = 0; i < 3; i++){
                window.draw(rectangles[i]);
        }
        window.display();
    }
    return 0;
}

