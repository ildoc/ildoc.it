Title: Get latest da codice di un progetto su TFS
Date: 2014-03-07 11:15:00
Modified: 2015-03-24 16:09:16
Tags: c#, get latest, tfs
Slug: get-latest-da-codice-di-un-progetto-su-tfs
Author: Doc

Sto scrivendo uno scriptino per, nell'ordine, ottenere l'ultima versione
di un progetto da TFS, buildarla e farne un publish su IIS.  
Al momento sono riuscito solo a fare il get latest e quasi il build...

Comunque ho potuto riscontrare della classicissima mancanza di
documentazione recente (e/o proprio di documentazione), quindi ecco qui
il mio piccolo contributo.

Questa funzione:

1.  si connette a un server tfs
2.  effettua l'autenticazione con username/password/dominio
3.  crea, se necessario, un workspace fittizio
4.  crea, se necessario, una cartella (o svuota quella indicata) nel
    filesystem
5.  mappa il workspace sulla cartella in questione
6.  scarica il codice da tfs
7.  cancella il workspace temporaneo

Per funzionare ha bisogno di aver referenziate le librerie
**Microsoft.TeamFoundation.Client** e
**Microsoft.TeamFoundation.VersionControl.Client**

    :::c#
    public void GetLatest()
    {
        TeamFoundationServer tfs;
        bool createdWorkspace = false;
        VersionControlServer versionControl;
        Workspace workspace = null;

        try
        {

            //Configurazione delle credenziali
            System.Net.NetworkCredential credential = new System.Net.NetworkCredential("username", "password", "dominio");

            //Configurazione del server
            string TFSServerPath = "http://server_di_tfs:8080";

            //Autenticazione nel tfs
            tfs = new TeamFoundationServer(TFSServerPath, credential);
            tfs.Authenticate();

            //Configurazione del workspace
            versionControl = (VersionControlServer)tfs.GetService(typeof(VersionControlServer));
            string workspaceName = "workspace_fittizio";

            //se il workspace è già mappato nel filesystem usa quello, altrimenti ne crea uno nuovo (che alla fine verrà cancellato)
            try
            {
                workspace = versionControl.GetWorkspace(workspaceName,
                                                        versionControl.AuthorizedUser);
            }
            catch (WorkspaceNotFoundException)
            {
                //Creazione workspace temporaneo");
                workspace = versionControl.CreateWorkspace(workspaceName,
                                                            versionControl.AuthorizedUser);
                createdWorkspace = true;
            }

            //Configurazione delle folder
            var serverFolder = "$/path/del/progetto/su/tfs";
            var localFolder = @"C:\cartella\dove\scaricare\il\progetto";

            //se la cartella non esiste la crea
            if (!Directory.Exists(localFolder))
                Directory.CreateDirectory(localFolder);

            //svuota la cartella di destinazione
            DirectoryInfo directory = new DirectoryInfo(localFolder);
            foreach (FileInfo file in directory.GetFiles("*", SearchOption.AllDirectories))
            {
                File.SetAttributes(file.FullName, FileAttributes.Normal);
                file.Delete();
            }
            foreach (DirectoryInfo subDirectory in directory.GetDirectories()) subDirectory.Delete(true);

            //Mapping del workspace
            var workingFolder = new WorkingFolder(serverFolder, localFolder);
            workspace.CreateMapping(workingFolder);

            if (!workspace.HasReadPermission)
            {
                throw new SecurityException(
                    String.Format("{0} does not have read permission for {1}",
                                    versionControl.AuthorizedUser, serverFolder));
            }

            //Esecuzione get latest
            workspace.Get(VersionSpec.Latest, GetOptions.Overwrite); //ci sono tipo 10 overload, fa anche il caffè
        }
        finally
        {
            //se è stato creato un workspace temporaneo viene cancellato
            if ((workspace != null) && createdWorkspace)
            {
                //Cancellazione workspace temporaneo
                workspace.Delete();
            }
        }
    }
