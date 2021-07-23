 #include "mbed.h"
#include "DHT.h"
 
DHT sensor(D2, DHT11);
 
int main()
{
    int error = 0;
    float h = 0.0f, c = 0.0f;
 
    while(1) {
        wait(2.0f);
        error = sensor.readData();
        if (0 == error) {
            c   = sensor.ReadTemperature(CELCIUS);
            h   = sensor.ReadHumidity();
            printf("Temp %f\r\n", c);
            printf("Hum %f\r\n", h);
        } else {
            printf("Error: %d\n", error);
        }
    }
}