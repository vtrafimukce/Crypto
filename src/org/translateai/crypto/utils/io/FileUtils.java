package org.translateai.crypto.utils.io;

import java.io.IOException;
import java.io.File;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Random;

public class FileUtils {
    private FileUtils() {
        //Prevent instantiation. This class contains only static methods.
    }
    public static byte[] readFile(String folderPath, String fileName) {
        Path path = Paths.get(folderPath, fileName);

        try {
            return Files.readAllBytes(path);
        } catch (IOException e) {
            throw new FileProcessingException("Error reading file: " + path, e);
        }
    }

    public static void writeFile(String folderPath, String fileName, byte[] data) {
        Path path = Paths.get(folderPath, fileName);

        try {
            Files.write(path, data);
        } catch (IOException e) {
            throw new FileProcessingException("Error writing file: " + path, e);
        }
    }

    public static String createTestSubFolder(String parentFolder) {
        String name = new SimpleDateFormat("yyyy-MM-dd-HH-mm-ss-")
                .format(new Date()) + new Random().nextInt(10000);
        boolean mkDirsResult = new File(parentFolder, name).mkdirs();
        String fullPath = Paths.get(parentFolder, name).toString();

        if (!mkDirsResult) {
            throw new FileProcessingException("Directory already exists: " + fullPath, null);
        }

        return fullPath;
    }

    public static boolean areEqual(String folder1, String file1,
                                String folder2, String file2) {
        Path path1 = Paths.get(folder1, file1);
        Path path2 = Paths.get(folder2, file2);

        try {
            return Files.mismatch(path1, path2) == -1;
        } catch (IOException e) {
            throw new FileProcessingException("Error comparing files: " +
                    path1 + " and " +
                    path2, e);
        }
    }
}
