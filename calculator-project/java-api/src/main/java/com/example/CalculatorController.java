package com.example;

import org.springframework.web.bind.annotation.*;
import org.springframework.http.ResponseEntity;
import java.io.*;

@RestController
public class CalculatorController {

    @GetMapping("/result")
    public ResponseEntity<String> getCalculationResult() {
        try (BufferedReader reader = new BufferedReader(new FileReader("result.txt"))) {
            String result = reader.readLine();
            return ResponseEntity.ok("Last calculated result: " + result);
        } catch (IOException e) {
            return ResponseEntity.status(500).body("Could not read result.");
        }
    }
}

