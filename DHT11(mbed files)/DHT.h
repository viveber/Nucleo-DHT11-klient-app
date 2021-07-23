
#ifndef MBED_DHT_H
#define MBED_DHT_H

#include "mbed.h"

typedef enum eType eType;
enum eType {
    DHT11     = 11,
    SEN11301P = 11,
    RHT01     = 11,
    DHT22     = 22,
    AM2302    = 22,
    SEN51035P = 22,
    RHT02     = 22,
    RHT03     = 22
};

typedef enum eError eError;
enum eError {
    ERROR_NONE = 0,
    BUS_BUSY,
    ERROR_NOT_PRESENT,
    ERROR_ACK_TOO_LONG,
    ERROR_SYNC_TIMEOUT,
    ERROR_DATA_TIMEOUT,
    ERROR_CHECKSUM,
    ERROR_NO_PATIENCE
};

typedef enum eScale eScale;
enum eScale {
    CELCIUS = 0,
    FARENHEIT,
    KELVIN
};


class DHT
{

public:

    DHT(PinName pin, eType DHTtype);
    ~DHT();
    eError readData(void);
    float ReadHumidity(void);
    float ReadTemperature(eScale const Scale);
    float CalcdewPoint(float const celsius, float const humidity);
    float CalcdewPointFast(float const celsius, float const humidity);

private:
    time_t  _lastReadTime;
    float _lastTemperature;
    float _lastHumidity;
    PinName _pin;
    bool _firsttime;
    eType _DHTtype;
    uint8_t DHT_data[5];
    float CalcTemperature();
    float CalcHumidity();
    float ConvertCelciustoFarenheit(float const);
    float ConvertCelciustoKelvin(float const);
    eError stall(DigitalInOut &io, int const level, int const max_time);

};

#endif
