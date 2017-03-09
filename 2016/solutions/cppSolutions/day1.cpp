//
// Created by Jarek Wojciechowski on 3/7/17.
//

#include "day1.h"
#include <iostream>
#include <fstream>
#include <vector>
#include <unordered_set>

struct Coordinate{
    int x;
    int y;
    Coordinate(int init_x, int init_y){ x = init_x; y = init_y;};
    bool operator==(const Coordinate& other) {
        return (x == other.x && y == other.y);
    }
};

template <>
struct std::hash<Coordinate>
{
    size_t operator()(Coordinate const & coord) const noexcept
    {
        return (
            (51 + std::hash<int>()(coord.x)) * 51
            + std::hash<int>()(coord.y)
        );
    }
};

class Compass{
    std::vector<Coordinate> cardinalVectors;
    int currentDirection = 0;
    Coordinate currentLocation = Coordinate(0,0);
    Coordinate firstIntersection = Coordinate(0,0);
    bool first_intersection_found = false;
    std::unordered_set<Coordinate> visitedCoordinates;
public:
    // Initalizes the cardinal directions vector x,y pairs used to correctly translate the movement distance
    Compass() {
        Coordinate north = Coordinate( 0, 1);
        Coordinate east  = Coordinate( 1, 0);
        Coordinate south = Coordinate( 0,-1);
        Coordinate west  = Coordinate(-1, 0);
        cardinalVectors = {north, east, west, south};
        visitedCoordinates.insert(Coordinate(0,0));
    }

    //Returns a pair representing the x,y movement multipliers to be applied to a distance to move
    Coordinate get_dir_vector(){ return cardinalVectors[currentDirection]; }

    //Increments or decrements the direction pointer intelligently to represent a "turn"
    void turn (char turn_direction){
        if (turn_direction == 'R'){ currentDirection = (currentDirection + 1) % 4; }
        else if (turn_direction == 'L'){ currentDirection = (currentDirection + 3) % 4; }
        else {std::cout << "Not sure how, but you turned a direction that isn't left or right";}
    }

    void record_intermediate_points(int xdiff, int ydiff){
        Coordinate coord_to_visit = currentLocation;
        int sign = (xdiff+ydiff)/(abs(xdiff+ydiff));

        //Only one of the values will ever be nonzero
        for(int i=0; i<abs(xdiff + ydiff); i++){
            //Get next point, modifying only one axis at a time
            if(xdiff>0){coord_to_visit.x += sign * 1;}
            else{coord_to_visit.y += sign * 1;}

            std::unordered_set<Coordinate>::const_iterator findResult = visitedCoordinates.find(coord_to_visit);
            //Check for a collision
            if (findResult != visitedCoordinates.end()) {
                //Save first intersection
                first_intersection_found = true;
                firstIntersection = coord_to_visit;
                return;
            }
            //Insert at the current location
            visitedCoordinates.insert(coord_to_visit);

        }
    }

    void move_distance(int distance){
        Coordinate dir_vector = get_dir_vector();
        int xdiff = distance * dir_vector.x;
        int ydiff = distance * dir_vector.y;
        if(!first_intersection_found)
            record_intermediate_points(xdiff, ydiff);
        currentLocation.x += xdiff;
        currentLocation.y += ydiff;
    }

    void apply_move(char direction, int distance){
        turn(direction);
        move_distance(distance);
    }

    int get_end_location(){ return abs(currentLocation.x) + abs(currentLocation.y);}
    int get_first_intersection(){ return abs(firstIntersection.x) + abs(firstIntersection.y);}
};


int solve_day1() {
    Compass compass = Compass();

    FILE *fp;
    if( (fp = fopen("day1input.txt", "r+")) == NULL) {
        printf("File doesn't exist\n");
        exit(1);
    }

    char turn_direction;
    int distance;

    fscanf(fp, "%c%d", &turn_direction, &distance);
    compass.apply_move(turn_direction, distance);

    while(fscanf(fp, ", %c%d", &turn_direction, &distance) == 2)
        compass.apply_move(turn_direction, distance);

    std::cout << "Manhattan Distance: " << compass.get_end_location();
    std::cout << "First intersection manhattan dist " << compass.get_first_intersection();
    return 0;
}
