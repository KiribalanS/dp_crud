package com.example;

import org.bson.Document;

import com.mongodb.client.MongoClient;
import com.mongodb.client.MongoClients;
import com.mongodb.client.MongoCollection;
import com.mongodb.client.MongoDatabase;
import com.mongodb.client.model.Filters;
import com.mongodb.client.model.Updates;

public class Main {


  public static void main(String[] args) {

    String uri = "YOUR MONGO URI";
    // Create a MongoClient
    try (MongoClient mongoClient = MongoClients.create(uri)) {
      } catch (Exception e) {
      System.out.print(e.toString());
    }
  }
}
