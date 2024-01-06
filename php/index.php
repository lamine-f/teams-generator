<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Team</title>

    <!-- Ajoutez le lien vers la feuille de style Bootstrap -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
</head>
<body>

    <div class="container mt-5">
        <div class="row justify-content-center">
            <div class="col-md-6">
                <form method="POST" action="" enctype="multipart/form-data">
                    <h2 class="text-center mb-4">Création de Groupes</h2>
                    
                    <div class="form-group">
                        <label for="team">Fichier d'équipe</label>
                        <input type="file" class="form-control-file" accept=".txt" name="team" id="team">
                    </div>
                    
                    <div class="form-group">
                        <label for="nombre">Nombre de groupes</label>
                        <input type="number" class="form-control" value="2" name="nombre" id="nombre" max="60" min="1">
                    </div>
                    
                    <button type="submit" class="btn btn-primary btn-block">Créer des groupes</button>
                </form>

                <?php
                if ($_SERVER['REQUEST_METHOD'] == "POST") {
                    if ($_FILES['team']['error'] == UPLOAD_ERR_OK) {
                        $file = $_FILES['team']['tmp_name'];
                        $nombre = filter_input(INPUT_POST, 'nombre', FILTER_VALIDATE_INT);

                        if ($nombre !== false && $nombre > 0) {
                            $students = file($file, FILE_IGNORE_NEW_LINES | FILE_SKIP_EMPTY_LINES);

                            if (count($students) >= $nombre) {
                                shuffle($students);

                                // Calculer la taille idéale de chaque groupe
                                $tailleGroupe = floor(count($students) / $nombre);

                                // Calculer le nombre d'élèves restants après la répartition équitable
                                $restants = count($students) % $nombre;

                                // Divise les élèves en groupes en ajustant la taille des groupes si nécessaire
                                $groupedStudents = [];
                                $start = 0;
                                for ($i = 0; $i < $nombre; $i++) {
                                    $end = $start + $tailleGroupe + ($restants > 0 ? 1 : 0);
                                    $groupedStudents[] = array_slice($students, $start, $end - $start);
                                    $start = $end;
                                    $restants--;
                                }

                                // Ouvre le fichier en mode append
                                $teamFile = fopen('team.txt', 'w');

                                $i = 1;
                                // Vous pouvez maintenant travailler avec les groupes de manière aléatoire
                                foreach ($groupedStudents as $group) {
                                    shuffle($group);
                                    fwrite($teamFile, "------------------------\n");
                                    fwrite($teamFile, "groupe " . $i . "\n");
                                    fwrite($teamFile, "\n");
                                    // $group contient maintenant un groupe d'élèves dans un ordre aléatoire
                                    // Écrit le groupe dans le fichier
                                    fwrite($teamFile, implode("\n", $group) . PHP_EOL);
                                    fwrite($teamFile, "\n");
                                    $i++;
                                }

                                // Ferme le fichier
                                fclose($teamFile);

                                echo '<div class="alert alert-success mt-3" role="alert">';
                                echo "Groupes ajoutés avec succès dans le fichier existant!";
                                echo '</div>';

                                echo '<p class="text-center mt-3">';
                                echo '<a href="team.txt" class="btn btn-secondary" target="_blank">Voir le fichier Team</a>';
                                echo '</p>';
                            } else {
                                echo '<div class="alert alert-danger mt-3" role="alert">';
                                echo "Il n'y a pas assez d'élèves pour créer des groupes de cette taille.";
                                echo '</div>';
                            }
                        } else {
                            echo '<div class="alert alert-danger mt-3" role="alert">';
                            echo "Nombre d'élèves invalide.";
                            echo '</div>';
                        }
                    } else {
                        echo '<div class="alert alert-danger mt-3" role="alert">';
                        echo "Erreur lors du téléchargement du fichier.";
                        echo '</div>';
                    }
                }
                ?>
            </div>
        </div>
    </div>

    <!-- Ajoutez le script Bootstrap JavaScript (facultatif, mais nécessaire pour certaines fonctionnalités) -->
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"></script>

</body>
</html>
