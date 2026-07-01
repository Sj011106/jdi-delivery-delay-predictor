package com.jdi.deliverypredictor;

public class DeliveryRequest {

    private double distance_km;
    private int weather_severity;
    private int road_type;
    private double cargo_weight_kg;
    private double driver_experience_yrs;
    private double departure_hour;
    private int season_fall;
    private int season_spring;
    private int season_summer;
    private int season_winter;

    // Getters
    public double getDistance_km()           { return distance_km; }
    public int getWeather_severity()         { return weather_severity; }
    public int getRoad_type()                { return road_type; }
    public double getCargo_weight_kg()       { return cargo_weight_kg; }
    public double getDriver_experience_yrs() { return driver_experience_yrs; }
    public double getDeparture_hour()        { return departure_hour; }
    public int getSeason_fall()              { return season_fall; }
    public int getSeason_spring()            { return season_spring; }
    public int getSeason_summer()            { return season_summer; }
    public int getSeason_winter()            { return season_winter; }

    // Setters
    public void setDistance_km(double v)           { this.distance_km = v; }
    public void setWeather_severity(int v)         { this.weather_severity = v; }
    public void setRoad_type(int v)                { this.road_type = v; }
    public void setCargo_weight_kg(double v)       { this.cargo_weight_kg = v; }
    public void setDriver_experience_yrs(double v) { this.driver_experience_yrs = v; }
    public void setDeparture_hour(double v)        { this.departure_hour = v; }
    public void setSeason_fall(int v)              { this.season_fall = v; }
    public void setSeason_spring(int v)            { this.season_spring = v; }
    public void setSeason_summer(int v)            { this.season_summer = v; }
    public void setSeason_winter(int v)            { this.season_winter = v; }
}