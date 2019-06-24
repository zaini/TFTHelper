package com.tfthelper.gui;

import javafx.fxml.*;
import javafx.scene.Scene;

/**
 * Class offering static methods to facilitate loading specific scenes/pages.
 * 
 * @author Francesco Compagnoni & Nerius Ilmonas
 * @version 2019.03.26
 */
public abstract class SceneLoader
{
    /**
     * Instantiates a scene using the FXMLLoader.
     * @param path The path of the desired FXML file.
     * @param origin Where to retrieve them from (simply pass in the instantiated
     * class requesting the new scene)
     * @return The new scene.
     * @throws Exception When the FXML file is not found an exception is thrown.
     */
    public static Scene getScene(String path, Class origin) throws Exception {
        return new Scene(FXMLLoader.load(origin.getResource(path)));
    }

    /**
     * Gets a loader for a specific scene, which allows for getting the
     * scene controller later on.
     * @param path The path of the desired FXML file.
     * @param origin Where to retrieve them from (simply pass in the instantiated
     * class requesting the new scene)
     * @return The FXML loader.
     * @throws Exception When the FXML file is not found an exception is thrown.
     */
    public static FXMLLoader getLoader(String path, Class origin) throws Exception {
        return new FXMLLoader(origin.getResource(path));
    }
}

