/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_atoi.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: agiron-d <agiron-d@student.42urduliz.co    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/01 22:11:03 by agiron-d          #+#    #+#             */
/*   Updated: 2025/12/01 23:47:10 by agiron-d         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

int	ft_is_space(int c)
{
	return ((c >= 9 && c <= 13) || c == 32);
}

static int	ft_isdigit(int c)
{
	return (c >= '0' && c <= '9');
}

static int	ft_isbtw(long nbr, int c)
{
	return ((nbr > INT_MAX || nbr < INT_MIN)
		|| (!ft_isdigit(c)
			&& !(ft_is_space(c) || c == 0)));
}

long	ft_atoi(const char *str)
{
	long	nbr;
	int		i;
	int		has_sign;

	nbr = 0;
	i = 0;
	has_sign = 1;
	while (ft_is_space(str[i]))
		i++;
	if (str[i] == '-' || str[i] == '+')
	{
		if (str[i] == '-')
			has_sign = -1;
		i++;
	}
	while (str[i] && ft_isdigit(str[i]))
		nbr = (nbr * 10) + (str[i++] - '0');
	if (ft_isbtw(nbr * has_sign, str[i]))
		ft_error();
	return (nbr * has_sign);
}
