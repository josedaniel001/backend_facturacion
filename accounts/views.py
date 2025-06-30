from django.contrib.auth.models import User, Group, Permission
from rest_framework import viewsets, filters, permissions,status
from rest_framework.permissions import IsAdminUser,IsAuthenticated
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .permissions import EsStaffOAdministradorGrupo
from .serializers import UserSerializer, UserCreateSerializer,GrupoSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]  # Protege el acceso

    def get_serializer_class(self):
        if self.action == 'create':
            return UserCreateSerializer
        return UserSerializer
    
class GrupoViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GrupoSerializer
    permission_classes = [EsStaffOAdministradorGrupo]  # Admins y staff pueden modificar roles

class RoleViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GrupoSerializer
    permission_classes = [EsStaffOAdministradorGrupo]

class PerfilUsuarioAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        grupos = user.groups.all()

        # Permisos estándar del sistema (auth_permission)
        permisos_sistema = Permission.objects.filter(group__user=user).values_list(
            'content_type__app_label', 'codename'
        ).distinct()

        permisos = [
            f"{app_label}.{codename}" for app_label, codename in permisos_sistema
        ]

        

        return Response({
            "id": user.id,
            "username": user.username,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "is_staff": user.is_staff,
            "groups": [g.name for g in grupos],
            "permissions": permisos,  # solo los permisos del sistema
            "role": grupos[0].name if grupos else None,
            "full_name": f"{user.first_name} {user.last_name}".strip(),
            "display_name": user.first_name or user.username,
            # Si el frontend también quiere verlos, puedes descomentar esto:
            #"custom_permissions": list(permisos_personalizados),
        })