package com.example.demo.controller;

import com.example.demo.model.User;
import com.fasterxml.jackson.core.type.TypeReference;
import com.fasterxml.jackson.databind.ObjectMapper;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.core.io.Resource;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.io.IOException;
import java.util.List;

@RestController
@RequestMapping("/api")
public class UserController {

    @Value("${app.data.file}")
    private Resource dataFile;

    private final ObjectMapper objectMapper;

    public UserController(ObjectMapper objectMapper) {
        this.objectMapper = objectMapper;
    }

    @GetMapping("/users")
    public ResponseEntity<List<User>> getUsers() {
        try {
            List<User> users = objectMapper.readValue(
                dataFile.getInputStream(),
                new TypeReference<List<User>>() {}
            );
            return ResponseEntity.ok(users);
        } catch (IOException e) {
            return ResponseEntity.internalServerError().build();
        }
    }
}

// Made with Bob
