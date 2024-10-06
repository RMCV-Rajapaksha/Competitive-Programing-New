#include <iostream>
#include <vector>
#include <cmath>
#include <tuple>

using namespace std;

// Function to calculate the distance between two points
double calculate_distance(double x1, double y1, double x2, double y2) {
    return sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1));
}

int main() {
    // Left gun parameters
    pair<double, double> left_gun_position = make_pair(-30, 0);
    double left_gun_speed = 60;

    // Right gun parameters
    pair<double, double> right_gun_position = make_pair(40, 0);
    double right_gun_speed = 50;

    // Input from console
    int n;  // Number of movements
    cin >> n;
    vector<tuple<int, int, int, int>> movements;

    // Getting movements data
    for (int i = 0; i < n; i++) {
        int initial_x, initial_y, final_x, final_y;
        cin >> initial_x >> initial_y >> final_x >> final_y;
        movements.push_back(make_tuple(initial_x, initial_y, final_x, final_y));
    }

    // To store the firing sequence
    vector<char> firing_sequence;

    // Times when the guns will be free
    double left_gun_free_time = 0;
    double right_gun_free_time = 0;

    // Current time (in seconds), starts from 0
    double current_time = 0;

    // Process each movement
    for (const auto& movement : movements) {
        int initial_x = get<0>(movement);
        int initial_y = get<1>(movement);
        int final_x = get<2>(movement);
        int final_y = get<3>(movement);

        // Check if the final position is below the end line (safe zone)
        if (final_y < 0) {
            continue;  // No shooting occurs for players below the end line
        }

        if (initial_x != final_x || initial_y != final_y) {  // Player moved
            // Calculate distances to both guns
            double distance_to_left_gun = calculate_distance(left_gun_position.first, left_gun_position.second, final_x, final_y);
            double distance_to_right_gun = calculate_distance(right_gun_position.first, right_gun_position.second, final_x, final_y);

            // Time for bullets to reach the player
            double time_for_left_bullet = distance_to_left_gun / left_gun_speed;
            double time_for_right_bullet = distance_to_right_gun / right_gun_speed;

            // Check which gun can shoot based on their busy times
            if (current_time >= left_gun_free_time) {
                // Left gun shoots if it's free
                firing_sequence.push_back('L');
                left_gun_free_time = current_time + time_for_left_bullet;
            } else if (current_time >= right_gun_free_time) {
                // Right gun shoots if it's free
                firing_sequence.push_back('R');
                right_gun_free_time = current_time + time_for_right_bullet;
            } else {
                // If both guns are busy, wait for the first available gun
                if (left_gun_free_time <= right_gun_free_time) {
                    // Left gun becomes available first
                    firing_sequence.push_back('L');
                    current_time = left_gun_free_time;  // Move time forward
                    left_gun_free_time += time_for_left_bullet;
                } else {
                    // Right gun becomes available first
                    firing_sequence.push_back('R');
                    current_time = right_gun_free_time;  // Move time forward
                    right_gun_free_time += time_for_right_bullet;
                }
            }
        } else {
            // No movement, no gun fires
            continue;
        }
    }

    // Output the firing sequence
    for (char gun : firing_sequence) {
        cout << gun << " ";
    }
    cout << endl;

    return 0;
}
