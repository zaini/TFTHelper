package com.tfthelper.gui;

import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.stage.Stage;


public class Main extends Application {

	@Override
	public void start(Stage stage) throws Exception {
		
		// Load initial stage
		FXMLLoader loader = SceneLoader.getLoader("layout/initial.fxml", getClass());
		Parent root = loader.load();
		
		//setup stage
		stage.setResizable(false);
		stage.setAlwaysOnTop(true);
		stage.setScene(new Scene(root));
		
		// show stage
		stage.show();
	}
}
