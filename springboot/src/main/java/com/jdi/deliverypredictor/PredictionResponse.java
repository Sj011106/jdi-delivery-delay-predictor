package com.jdi.deliverypredictor;

public class PredictionResponse {

    private boolean delayed;
    private double probability;
    private String message;

    // Constructor
    public PredictionResponse(boolean delayed,
                              double probability,
                              String message) {
        this.delayed     = delayed;
        this.probability = probability;
        this.message     = message;
    }

    // Getters
    public boolean isDelayed()       { return delayed; }
    public double getProbability()   { return probability; }
    public String getMessage()       { return message; }
}