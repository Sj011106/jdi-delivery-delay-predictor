package com.jdi.deliverypredictor;

import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.client.RestTemplate;
import org.springframework.http.HttpEntity;
import org.springframework.http.HttpHeaders;
import org.springframework.http.MediaType;

@RestController
@RequestMapping("/api")
public class DeliveryController {

    // RestTemplate is Spring's tool for calling other APIs
    private final RestTemplate restTemplate = new RestTemplate();

    // URL of your Flask API
    private final String FLASK_URL = "http://localhost:5000/predict";

    @PostMapping("/predict")
    public ResponseEntity<PredictionResponse> predict(
            @RequestBody DeliveryRequest deliveryRequest) {

        // Step 1 — Set up headers for JSON request
        HttpHeaders headers = new HttpHeaders();
        headers.setContentType(MediaType.APPLICATION_JSON);

        // Step 2 — Wrap request with headers
        HttpEntity<DeliveryRequest> entity =
                new HttpEntity<>(deliveryRequest, headers);

        // Step 3 — Call Flask API and get response
        ResponseEntity<PredictionResponse> flaskResponse =
                restTemplate.postForEntity(
                        FLASK_URL,
                        entity,
                        PredictionResponse.class
                );

        // Step 4 — Return Flask response back to caller
        return ResponseEntity.ok(flaskResponse.getBody());
    }
}