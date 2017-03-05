#include <iostream>
#include <fstream>
#include <map>
#include <vector>

class Compass{
    std::vector<std::pair<int,int>> cardinalVectors;
    int currentDirection = 0;
public:
    // Initalizes the cardinal directions vector with pairs that represent x,y coordinate pairs
    Compass() {
        std::pair<int, int> north = std::make_pair( 0, 1);
        std::pair<int, int> east  = std::make_pair( 1, 0);
        std::pair<int, int> south = std::make_pair( 0,-1);
        std::pair<int, int> west  = std::make_pair(-1, 0);
        cardinalVectors = {north, east, west, south};
    }

    //Returns a pair representing the x,y movement multipliers to be applied to a distance to move
    std::pair<int, int> get_dir_vector(){ return cardinalVectors[currentDirection]; }

    //Increments or decrements the direction pointer intelligently to represent a "turn"
    void turn (std::string turn_direction){
        if (turn_direction == "R"){ currentDirection = (currentDirection + 1) % 4; }
        else if (turn_direction == "L"){ currentDirection = (currentDirection - 1) % 4;}
        else {std::cout << "Not sure how, but you turned a direction that isn't left or right";}
    }
};

int main() {
    Compass compass = Compass();

    FILE *fp;
    if( (fp = fopen("day1input.txt", "r+")) == NULL) {
        printf("No such file\n");
        exit(1);
    }

    char turn_direction;
    int distance;
    fscanf(fp, "%c%d", &turn_direction, &distance);
    std::cout << turn_direction << " " << distance << "\n";

    while(fscanf(fp, ", %c%d", &turn_direction, &distance) == 2) {
        std::cout << turn_direction << " " << distance << "\n";
        int i = 0;
    }
    return 0;
}
